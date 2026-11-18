---
title: "Abc conjecture"
date: '2025-02-21T16:36:00+00:00'
category: webclip
summary: 'Overview of the abc conjecture in number theory: its formal formulations, examples, known bounds, wide-ranging consequences, computational searches, refinements, and the disputed proof claim by Mochizuki.'
tags: ["number-theory", "conjectures", "diophantine-equations", "elliptic-curves"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Abc conjecture"
    url: "https://en.wikipedia.org/wiki/Abc_conjecture"
    kind: wiki
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/en-wikipedia-org--abc-conjecture-number-theory-overview.md"
    kind: repo
---

The abc conjecture (Oesterlé–Masser conjecture) is a central open problem in number theory, formulated in 1985 by Joseph Oesterlé and David Masser. It concerns coprime positive integers a, b, c with a + b = c and relates c to the radical rad(abc), the product of the distinct prime factors of abc. Roughly, it says that rad(abc) is not often much smaller than c and provides several equivalent formulations in terms of inequalities involving rad(abc) and the quality q(a, b, c) = log c / log rad(abc). Typical triples have c < rad(abc), while triples with q > 1 are rare and involve high powers of small primes. The conjecture is equivalent to a modified form of Szpiro's conjecture and has many deep consequences, including implications for Roth's theorem, the Mordell conjecture, Fermat's Last Theorem, the Fermat–Catalan conjecture, and others.

The article describes examples of triples with small radicals, techniques to construct families where rad(abc) is arbitrarily small relative to c, and lists some of the highest-quality known triples, such as a triple with quality about 1.6299 found by Eric Reyssat. Theoretical work has produced exponential upper bounds for c in terms of rad(abc), and lower-bound results show that any eventual abc inequality must allow infinitely many triples with relatively large c compared to rad(abc). A distributed computing project, ABC@Home, has searched for many triples with rad(abc) < c and compiled data on the distribution of qualities. Several refinements and strengthened forms of the conjecture have been proposed, including Baker's versions and inequalities involving the number of prime factors. Shinichi Mochizuki has claimed a proof via inter-universal Teichmüller theory and a proof of Szpiro's conjecture, but leading experts have identified what they regard as a serious gap, so the conjecture remains widely considered unproven despite the eventual publication of his work.

## Reading notes

- The abc conjecture is a conjecture in number theory due to Joseph Oesterlé and David Masser, originating from their attempts to understand Szpiro's conjecture about elliptic curves in 1985.
- It is formulated for coprime positive integers a, b, c with a + b = c and relates c to rad(abc), the product of distinct prime factors of abc.
- The conjecture states that for every positive real ε there are only finitely many such triples with c larger than a fixed power of rad(abc) depending on ε.
- An equivalent version asserts that for every ε > 0 there exists a constant Kε such that c is bounded above by Kε · rad(abc)^{1+ε} for all coprime triples with a + b = c.
- Using little-o notation, an equivalent statement is that for all coprime triples with a + b = c, rad(abc) is at least c^{1−o(1)}.
- Another equivalent formulation uses the quality q(a, b, c) = log c / log rad(abc); the conjecture says that for every ε > 0 only finitely many triples with a + b = c satisfy q(a, b, c) > 1 + ε.
- Typical coprime triples with a + b = c satisfy c < rad(abc), so q(a, b, c) < 1, while triples with q > 1 involve numbers divisible by high powers of small primes.
- Although there are infinitely many coprime triples with a + b = c and q(a, b, c) > 1, the conjecture predicts only finitely many with q exceeding any fixed threshold greater than 1, such as 1.01 or 1.001.
- If the conjecture holds, there must exist a triple (a, b, c) that attains the maximal possible quality q(a, b, c).
- The condition ε > 0 in the main inequality is necessary because there are infinitely many triples with c > rad(abc), constructed so that b has large square factors.
- The article sketches a construction where, by choosing exponents so that b is divisible by a prime square (first for 9 dividing b, then for p² dividing b using Fermat's little theorem), the ratio rad(abc)/c can be made arbitrarily small.
- A list of highest-quality triples includes an example found by Eric Reyssat with a = 2, b = 3¹⁰·109, c = 2³⁵, rad(abc) = 15042, and quality approximately 1.6299.
- The conjecture implies numerous important results, such as Roth's theorem on Diophantine approximation of algebraic numbers and the Mordell conjecture (already proved by Gerd Faltings).
- It is equivalent to Vojta's conjecture in dimension 1 and to the modified Szpiro conjecture, which would yield a bound of approximately rad(abc)^{1.2+ε}.
- Other consequences include statements about the Erdős–Woods conjecture with only finitely many counterexamples and the existence of infinitely many non-Wieferich primes in every base b > 1.
- A weak form of Marshall Hall's conjecture on the separation between squares and cubes of integers follows from the abc conjecture.
- Fermat's Last Theorem, which has a difficult proof by Andrew Wiles, would follow easily for large exponents from an effective weak form of abc, assuming a finite upper bound on quality such as 2.
- The conjecture would also imply results on the Fermat–Catalan conjecture concerning sums of powers and properties of Dirichlet L-functions, including the absence of Siegel zeros under a uniform form over number fields.
- It yields finiteness results for perfect powers taken by polynomials with at least three simple zeros when evaluated at integer arguments.
- A generalization of Tijdeman's theorem and Pillai's conjecture concerning solutions to equations of the form y^m = x^n + k or A y^m = B x^n + k would follow from abc.
- The Granville–Langevin conjecture, equivalent to abc, predicts lower bounds on the radical of values of square-free binary forms in terms of max{|x|, |y|} raised to a power depending on the degree.
- Under abc, polynomials of the form (x^n − 1)/(x − 1) are predicted to take infinitely many square-free values.
- Dąbrowski showed that abc would imply that for any fixed integer A, the Diophantine equation n! + A = k² has only finitely many solutions.
- Granville proved that abc would give an asymptotic count for n up to N such that a given polynomial evaluated at n, after dividing by a fixed integer, is square-free, with an explicit positive density constant.
- The Beal conjecture, a generalization of Fermat's Last Theorem about equations A^x + B^y = C^z with exponents greater than 2, would follow in the sense that abc implies only finitely many counterexamples.
- Lang's conjecture about lower bounds for the Néron–Tate height of non-torsion rational points on elliptic curves is listed as another consequence.
- The abc conjecture would yield a negative solution to the Erdős–Ulam problem on dense sets of Euclidean points with rational distances.
- It would also give an effective version of Siegel's theorem on integral points on algebraic curves.
- Existing unconditional results show that abc would allow c to be bounded above by a function of rad(abc) that is close to linear, while currently known general upper bounds for c in terms of rad(abc) are exponential.
- In these known bounds, the involved constants do not depend on a, b, c (except for one depending on ε) and the inequalities hold for triples with c > 2.
- Lower-bound work by Stewart and Tijdeman shows there are infinitely many coprime triples with a + b = c where c is at least rad(abc) raised to a power k for any k less than 4, later improved to about 6.068.
- The ABC@Home grid computing project, started by Leiden University and Dutch Kennislink in 2006, searches for triples with rad(abc) < c to study patterns, though such computations cannot prove or disprove the conjecture.
- Computational data include counts of triples with quality greater than various thresholds (such as 1, 1.05, 1.1, 1.2, 1.3, 1.4) for c below powers of 10 up to 10¹⁸.
- As of May 2014, ABC@Home reported having found about 23.8 million triples with rad(abc) < c.
- A short table lists five highest-quality triples with their a, b, c and discoverers, including work by Reyssat, Benne de Weger, and Browkin, Brzezinski, and Nitaj.
- The abc conjecture is described as an integer analogue of the Mason–Stothers theorem for polynomials.
- Baker proposed a strengthening where rad(abc) in the abc inequality is replaced by ε^{−ω} rad(abc), with ω the number of distinct primes dividing a, b, c.
- Andrew Granville observed that a particular function related to these refinements attains its minimum at a specific configuration, which led Baker to propose an "explicit abc conjecture" involving an inequality with a constant κ.
- Baker reported that computational experiments suggested a specific admissible value for κ in his explicit version.
- Baker also discussed related conjectures of Granville that would bound c using Ω(n), the total number of prime factors of n, or using Θ(n), the count of integers up to n with all prime divisors among those dividing n.
- Robert, Stewart, and Tenenbaum proposed a more precise inequality depending on k = rad(abc), conjecturing that c is always below an expression involving exp(C₁ √(log k · log log k)) and that another similar expression with a different constant holds infinitely often.
- Browkin and Brzeziński introduced the n conjecture, a generalization of abc to more than three integers, requiring n > 2.
- Lucien Szpiro proposed a solution to the conjecture in 2007, but it was subsequently found incorrect.
- In 2012, Shinichi Mochizuki released four preprints claiming a proof of Szpiro's conjecture and thus abc, based on his inter-universal Teichmüller theory (IUTT).
- Despite these claims, the papers have not been broadly accepted as a proof due to their length, difficulty, and what several experts identify as a gap in the argument.
- Some mathematicians have publicly supported Mochizuki's work and helped organize workshops on IUTT, but these efforts did not persuade most number theorists.
- In March 2018, Peter Scholze and Jakob Stix visited Kyoto to discuss the proof with Mochizuki, after which they wrote a report arguing that the gap in the proof is severe and cannot be fixed by small changes.
- Mochizuki responded that Scholze and Stix misunderstood essential aspects of his theory and that their simplifications were invalid, publishing his own detailed reports of the discussions.
- In April 2020, the Research Institute for Mathematical Sciences in Kyoto announced that Mochizuki's work would appear in its journal, with Mochizuki recusing himself as editor for the review process.
- Commentators such as Kiran Kedlaya and Edward Frenkel, and an article in Nature, expressed skepticism that publication in RIMS would change the community's stance on the proof.
- Mochizuki's claimed proof appeared in RIMS in March 2021, but other sources referenced in the article still state that the abc conjecture is regarded as unproven.
- The article places the abc conjecture among the major unsolved problems in mathematics and quotes Dorian Goldfeld describing it as the most important unsolved problem in Diophantine analysis.
