---
url: "https://mccue.dev/pages/3-11-25-life-altering-postgresql-patterns?utm_source=tldrnewsletter"
captured_at: "2026-09-25T17:54:07+01:00"
title: "Life Altering Postgresql Patterns"
domain: "mccue-dev"
---

by: **Ethan McCue**

Believe it or not, I don't think that title is clickbait.

There is a set of things that you can do when working with a Postgres database which I have found made my and my coworker's lives much more pleasant. Each one is by itself small, but in aggregate have a noticeable effect.

## Use UUID primary keys

UUIDs have downsides

*   Truly random UUIDs doesn't sort well (and this has implications for indexes)
*   They take up more space than sequential ids (space being your cheapest resource)

But I've found those to be far outweighed by the upsides

*   You don't need to coordinate with the database to produce one.
*   They are safe to share externally.

```
CREATE TABLE person(
    id uuid not null default gen_random_uuid() primary key,
    name text not null
)
```

## Give everything created\_at and updated\_at

It's not a full history, but knowing when a record was created or last changed is a useful breadcrumb when debugging. Its also something you can't retroactively get unless you were recording it.

So just always slap a `created_at` and `updated_at` on your tables. You can maintain `updated_at` automatically with a trigger.

```
CREATE TABLE person(
    id uuid not null default gen_random_uuid() primary key,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now(),
    name text not null
);

CREATE FUNCTION set_current_timestamp_updated_at()
    RETURNS TRIGGER AS $$
DECLARE
_new record;
BEGIN
  _new := NEW;
  _new."updated_at" = now();
RETURN _new;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_person_updated_at
    BEFORE UPDATE ON person
    FOR EACH ROW
    EXECUTE PROCEDURE set_current_timestamp_updated_at();
```

You need to create the trigger for each table, but you only need to create the function once.

## on update **restrict** on delete **restrict**

When you make a foreign key constraint on a table, always mark it with `on update restrict on delete restrict`.

This makes it so that if you try and delete the referenced row you will get an error. Storage is cheap, recovering data is a nightmare. Better to error than do something like `cascade`.

```
CREATE TABLE person(
    id uuid not null default gen_random_uuid() primary key,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now(),
    name text not null
);

CREATE TABLE pet(
    id uuid not null default gen_random_uuid() primary key,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now(),
    name text not null,
    owner_id uuid not null references person(id)
                on update restrict
                on delete restrict
);
```

## Use schemas

By default, every table in Postgres will go into the "`public`" schema. This is _fine_, but you are missing out if you don't take advantage of your ability to make new schemas.

Schemas work as namespaces for tables and for any moderate to large app you are going to have a lot of tables. You can do joins and have relationships between tables in different schemas so there isn't much of a downside.

```
CREATE SCHEMA vet;

CREATE TABLE vet.person(
    id uuid not null default gen_random_uuid() primary key,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now(),
    name text not null
);

CREATE TABLE vet.pet(
    id uuid not null default gen_random_uuid() primary key,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now(),
    name text not null,
    owner_id uuid not null references vet.person(id)
                on update restrict
                on delete restrict
);
```

## Enum Tables

There are a lot of ways to make "enums" in sql. One is to use the actual "[enum types](https://www.postgresql.org/docs/current/datatype-enum.html)," another is to use a [check constraint](https://www.postgresql.org/docs/current/ddl-constraints.html).

The pattern introduced to me [by Hasura](https://hasura.io/) was enum tables.

Have a table with some `text` value as a primary key and make columns in other tables reference it with a foreign key.

```
CREATE TABLE vet.pet_kind(
    value text not null primary key
);

INSERT INTO vet.pet_kind(value)
VALUES ('dog'), ('cat'), ('bird');

CREATE TABLE vet.pet(
    id uuid not null default gen_random_uuid() primary key,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now(),
    owner_id uuid not null references vet.person(id)
                on update restrict
                on delete restrict,
    kind text not null references vet.pet_kind(value)
                on update restrict
                on delete restrict
);
```

This way you can insert into a table to add more allowed values or attach metadata like a comment to explain what each value means.

```
CREATE TABLE vet.pet_kind(
    value text not null primary key,
    comment text not null default ''
);

INSERT INTO vet.pet_kind(value, comment)
VALUES 
    ('dog', 'A Canine'),
    ('cat', 'A Feline'),
    ('bird', 'A 50 Year Commitment');

CREATE TABLE vet.pet(
    id uuid not null default gen_random_uuid() primary key,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now(),
    owner_id uuid not null references vet.person(id)
                on update restrict
                on delete restrict,
    kind text not null references vet.pet_kind(value)
                on update restrict
                on delete restrict
);
```

## Name your tables singularly

This isn't even Postgres specific, just please name your tables using the singular form of a noun.

`SELECT * FROM pets` might seem nicer than `SELECT * FROM pet` but the moment you start doing anything more interesting with your queries you will notice that your queries are actually working in terms of individual rows.

```
SELECT *
FROM pet
-- It's a cruel coincidence that in english an "s"
-- suffix can sometimes work both as a plural
-- and a possessive, but notice how the where clause
-- is asserting a condition about a single row.
WHERE pet.name = 'sally' 
```

The deeper you dig the more annoying edge cases you'll run into with plural table names. Just name your tables the same as what an individual row in that table represents.

## Mechanically name join tables

Sometimes there are sensible names to give "join tables" - tables which form the basis for "many to many" relationships between data - but often there isn't. In those cases don't hesitate to just concatenate the names of the tables you are joining between.

```
CREATE TABLE vet.person(
    id uuid not null default gen_random_uuid() primary key,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);

CREATE TABLE vet.pet(
    id uuid not null default gen_random_uuid() primary key,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);

-- pet_owner would work in this context, but
-- I just want to demonstrate the table_a_table_b naming scheme
CREATE TABLE vet.person_pet(
    id uuid not null default gen_random_uuid() primary key,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now(),
    person_id uuid not null references vet.person(id)
                on update restrict
                on delete restrict,
    pet_id uuid not null references vet.pet(id)
                on update restrict
                on delete restrict
);

CREATE UNIQUE INDEX ON vet.person_pet(person_id, pet_id);
```

## Almost always soft delete

I will reiterate that storage is cheap and recovering data is a nightmare.

If you have some domain specific need to delete (or otherwise mark as irrelevant) some data, use a nullable `timestamptz` column. If there is a timestamp filled in, that's when it was deleted. If there is no timestamp it isn't deleted yet.

```
CREATE TABLE vet.prescription(
    id uuid not null default gen_random_uuid() primary key,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now(),
    pet_id uuid not null references vet.pet(id)
             on update restrict
             on delete restrict,
    issued_at timestamptz not null,
    -- Instead of deleting a prescription,
    -- explicitly mark when it was revoked
    revoked_at timestamptz
);
```

Even outside the context of a soft delete, timestamps are usually more useful than a boolean. If you want to know whether something happened, you generally also want to know when it happened.

## Represent statuses as a log

It is very tempting to represent the status of something as a single column. You submit some paperwork and it has a `status` of `submitted`. Someone starts to look at it then it transitions to `in_review`. From there maybe its `rejected` or `approved`.

There are two problems with this

1.  You might actually care about when it was `approved`, or by whom.
2.  You might receive this information out-of-order.

Webhooks are a prime example of the 2nd situation. There's no way in the laws of physics to be sure you'll get events in exactly the right order.

To handle this you should have a table where each row represents the status of the thing at a given point in time. Instead of overloading `created_at` or `updated_at` for this, have an explicit `valid_at` which says when that information is valid for.

```
CREATE TABLE vet.adoption_approval_status(
    value text not null primary key
);

INSERT INTO vet.adoption_approval_status(value)
VALUES ('submitted'), ('in_review'), ('rejected'), ('approved');

CREATE TABLE vet.adoption_approval(
    id uuid not null default gen_random_uuid() primary key,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now(),
    person_id uuid not null references vet.person(id)
                on update restrict
                on delete restrict,
    status text not null references vet.adoption_approval_status(value)
                on update restrict
                on delete restrict,
    valid_at timestamptz not null
);

CREATE INDEX ON vet.adoption_approval(person_id, valid_at DESC);
```

Just having an index on `valid_at` can work for a while, but eventually your queries will get too slow. There are a lot of ways to handle this, but the one we've found that works the best is to have an explicit `latest` column with a cheeky unique index and trigger to make sure that only the row with the newest `valid_at` is the `latest` one.

```
CREATE TABLE vet.adoption_approval(
    id uuid not null default gen_random_uuid() primary key,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now(),
    person_id uuid not null references vet.person(id)
                on update restrict
                on delete restrict,
    status text not null references vet.adoption_approval_status(value)
                on update restrict
                on delete restrict,
    valid_at timestamptz not null,
    latest boolean default false
);

CREATE INDEX ON vet.adoption_approval(person_id, valid_at DESC);

-- Conditional unique index makes sure we only have one latest
CREATE UNIQUE INDEX ON vet.adoption_approval(person_id, latest)
WHERE latest = true;

-- Then a trigger to keep latest up to date
CREATE OR REPLACE FUNCTION vet.set_adoption_approval_latest()
 RETURNS trigger
 LANGUAGE plpgsql
AS $function$
BEGIN
    UPDATE vet.adoption_approval
    SET latest = false
    WHERE latest = true and person_id = NEW.person_id;

    UPDATE vet.adoption_approval
    SET latest = true
    WHERE id = (
        SELECT id 
        FROM vet.adoption_approval 
        WHERE person_id = NEW.person_id
        ORDER BY valid_at DESC 
        LIMIT 1
    );

    RETURN null;
END;
$function$;

CREATE TRIGGER adoption_approval_insert_trigger
    AFTER INSERT ON vet.adoption_approval
    FOR EACH ROW
    EXECUTE FUNCTION vet.set_adoption_approval_latest();
```

## Mark special rows with a `system_id`

It's not uncommon to end up with "special rows." By this I mean rows in a table that the rest of your system will rely on the presence of to build up behavior.

All rows in an enum table are like this, but you will also end up with rows in tables of otherwise normal "generated during the course of normal use" rows. For these, give them a special `system_id`.

Unique indexes don't mind multiple rows with null values, so you can make a unique index on this `system_id` and look up your special rows later as you need to.

```
CREATE TABLE vet.contact_info(
    id uuid not null default gen_random_uuid() primary key,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now(),
    person_id uuid references vet.person(id)
                on update restrict
                on delete restrict,
    mailing_address text not null,
    system_id text
);

CREATE UNIQUE INDEX ON vet.contact_info(system_id);

-- Not hard to imagine wanting to build functionality that
-- automatically contacts the CDC for cases of rabies or similar,
-- but maybe every other bit of contact_info in the system is
-- for more "normal" purposes
INSERT INTO vet.contact_info(system_id, mailing_address)
VALUES ('cdc', '4770 Buford Highway, NE');
```

## Use views sparingly

Views are amazing and terrible.

They are amazing in their ability to wrap up a relatively complex or error-prone query into something that looks basically like a table.

They are terrible in that removing obsolete columns requires a drop and recreation, which can become a nightmare when you build views on views. The query planner also seems to have trouble seeing through them in general.

So do use views, but only as many as you need and be [very wary](https://www.youtube.com/watch?v=CLnADKgurvc) of building views on views.

```
CREATE TABLE vet.prescription(
    id uuid not null default gen_random_uuid() primary key,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now(),
    pet_id uuid not null references vet.pet(id)
             on update restrict
             on delete restrict,
    issued_at timestamptz not null,
    -- Instead of deleting a prescription,
    -- explicitly mark when it was revoked
    revoked_at timestamptz
);

CREATE INDEX ON vet.prescription(revoked_at);

-- There are pros and cons to having this view
CREATE VIEW vet.active_prescription AS
    SELECT
        vet.prescription.id,
        vet.prescription.created_at,
        vet.prescription.updated_at,
        vet.prescription.pet_id,
        vet.prescription.issued_at
    FROM
        vet.prescription
    WHERE 
        vet.prescription.revoked_at IS NULL;
```

## JSON Queries

You might have heard that Postgres "supports JSON." This is true, but I had mostly heard it in the context of storing and querying JSON. If you want a table with some blob of info slap a `jsonb` column on one your tables.

That is neat, but I've gotten way more mileage out of using JSON as the result of a query. This has definite downsides like losing type information, needing to realize your results all at once, and the overhead of writing into json.

But the giant upside is that you can get all the information you want from the database in **one trip**, no cartesian product nightmares or N+1 problems in sight.

```
SELECT jsonb_build_object(
  'id', vet.person.id,
  'name', vet.person.name,
  'pets', array(
    SELECT jsonb_build_object(
      'id', vet.pet.id,
      'name', vet.pet.name,
      'prescriptions', array(
        SELECT jsonb_build_object(
          'issued_at', vet.prescription.issued_at
        )
        FROM vet.prescription
        WHERE vet.prescription.pet_id = vet.pet.id
      )
    )
    FROM vet.person_pet
    LEFT JOIN vet.pet 
      ON vet.pet.id = vet.person_pet.pet_id
    WHERE vet.person_pet.person_id = vet.person.id
  ),
  'contact_infos', array(
    SELECT jsonb_build_object(
      'mailing_address', vet.contact_info.mailing_address
    )
    FROM vet.contact_info
    WHERE vet.contact_info.person_id = vet.person.id
  )
) 
FROM vet.person
WHERE id = '29168a93-cd14-478f-8c70-a2b7a782c714';
```

Which can net you something like the following.

```
{
  "id": "29168a93-cd14-478f-8c70-a2b7a782c714",
  "name": "Jeff Computers",
  "pets": [
    {
      "id": "3e5557c0-c628-44ef-b4d1-86012c5f48bf",
      "name": "Rhodie",
      "prescriptions": [
        {
          "issued_at": "2025-03-11T23:46:18.345146+00:00"
        }
      ]
    },
    {
      "id": "ed63ca7d-3368-4353-9747-6b6b2fa6657a",
      "name": "Jenny",
      "prescriptions": []
    }
  ],
  "contact_infos": [
    {
      "mailing_address": "123 Sesame St."
    }
  ]
}
```

You can find all the setup you'd need to do for that query [here](https://gist.github.com/bowbahdoe/dee0a5d534d9a36c677dbf0de977b6de). You can try it out on [](https://onecompiler.com/postgresql)[https://onecompiler.com/postgresql](https://onecompiler.com/postgresql) if setting up a local postgres is a bit much.

* * *

If there is something I missed or got wrong, tell me very loudly in person or here on the internet.

* * *

#### [<- Index](https://mccue.dev/)
