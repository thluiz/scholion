---
url: "http://etodd.io/2015/09/28/one-weird-trick-better-code/?utm_content=buffere19c0&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer"
captured_at: "2016-01-02T14:03:36-03:00"
title: "One Weird Trick to Write Better Code · Evan Todd"
domain: "etodd-io"
---

# One Weird Trick to Write Better Code · Evan Todd

```
class idEntity  public idClass 
public
    static const         MAX_PVS_AREAS  
    static const uint32        INVALID_PREDICTION_KEY  0xFFFFFFFF

                            entityNumber            // index into the entity list
                            entityDefNumber        // index into the entity def list

    idLinkListidEntity    spawnNode                // for being linked into spawnedEntities list
    idLinkListidEntity    activeNode                // for being linked into activeEntities list
    idLinkListidEntity    aimAssistNode            // linked into gameLocal.aimAssistEntities

    idLinkListidEntity    snapshotNode            // for being linked into snapshotEntities list
                            snapshotChanged        // used to detect snapshot state changes
                            snapshotBits            // number of bits this entity occupied in the last snapshot
                        snapshotStale            // Set to true if this entity is considered stale in the snapshot

    idStr                                        // name of entity
    idDict                    spawnArgs                // key/value pairs used to spawn and initialize entity
    idScriptObject            scriptObject            // contains all script defined data for this entity

                            thinkFlags                // TH_? flags
                            dormantStart            // time that the entity was first closed off from player
                        cinematic                // during cinematics, entity will only think if cinematic is set

    renderView_t             renderView                // for camera views from this entity
    idEntity                 cameraTarget            // any remoteRenderMap shaders will use this

    idList idEntityPtridEntity TAG_ENTITY     targets        // when this entity is activated these entities entity are activated

                            health                    // FIXME: do all objects really need health?

    struct entityFlags_s 
                        notarget                // if true never attack or target this entity
                        noknockback                // if true no knockback from hits
                        takedamage                // if true this entity can be damaged
                        hidden                    // if true this entity is not visible
                        bindOrientated            // if true both the master orientation is used for binding
                        solidForTeam            // if true this entity is considered solid when a physics team mate pushes entities
                        forcePhysicsUpdate        // if true always update from the physics whether the object moved or not
                        selected                // if true the entity is selected for editing
                        neverDormant            // if true the entity never goes dormant
                        isDormant                // if true the entity is dormant
                        hasAwakened                // before a monster has been awakened the first time, use full PVS for dormant instead of area-connected
                        networkSync             // if true the entity is synchronized over the network
                        grabbed                    // if true object is currently being grabbed
                        skipReplication         // don't replicate this entity over the network.
     

                            timeGroup

                        noGrab

    renderEntity_t            xrayEntity
    qhandle_t                xrayEntityHandle
    const idDeclSkin         xraySkin

                        DetermineTimeGroup  slowmo 

                        SetGrabbedState  grabbed 
                        IsGrabbed

public
    ABSTRACT_PROTOTYPE idEntity 

                            idEntity
                            idEntity

                        Spawn

                         idSaveGame savefile  const
                        Restore idRestoreGame savefile 

    const              GetEntityDefName const
                        SetName const   
    const              GetName const
    virtual             UpdateChangeableSpawnArgs const idDict source 
                            GetEntityNumber const  return entityNumber 

                            // clients generate views based on all the player specific options,
                            // cameras have custom code, and everything else just uses the axis orientation
    virtual renderView_t     GetRenderView

    // thinking
    virtual             Think
                        CheckDormant    // dormant == on the active list, but out of PVS
    virtual                DormantBegin    // called when entity becomes dormant
    virtual                DormantEnd        // called when entity wakes from being dormant
                        IsActive const
                        BecomeActive  flags 
                        BecomeInactive  flags 
                        UpdatePVSAreas const idVec3  
                        BecomeReplicated

    // visuals
    virtual             Present
    virtual renderEntity_t GetRenderEntity
    virtual                 GetModelDefHandle
    virtual             SetModel const  modelname 
                        SetSkin const idDeclSkin  
    const idDeclSkin         GetSkin const
                        SetShaderParm  parmnum float value 
    virtual             SetColor float  float green float  
    virtual             SetColor const idVec3 color 
    virtual             GetColor idVec3   const
    virtual             SetColor const idVec4 color 
    virtual             GetColor idVec4   const
    virtual             FreeModelDef
    virtual             FreeLightDef
    virtual             
    virtual             
                        IsHidden const
                        UpdateVisuals
                        UpdateModel
                        UpdateModelTransform
    virtual             ProjectOverlay const idVec3 origin const idVec3  float  const  material 
                            GetNumPVSAreas
    const                  GetPVSAreas
                        ClearPVSAreas
                        PhysicsTeamInPVS pvsHandle_t pvsHandle 

    // animation
    virtual             UpdateAnimationControllers
                        UpdateRenderEntity renderEntity_s renderEntity const renderView_t renderView 
    static                 ModelCallback renderEntity_s renderEntity const renderView_t renderView 
    virtual idAnimator     GetAnimator    // returns animator object used by this entity

    // sound
    virtual             CanPlayChatterSounds const
                        StartSound const  soundName const s_channelType channel  soundShaderFlags  broadcast  length 
                        StartSoundShader const idSoundShader shader const s_channelType channel  soundShaderFlags  broadcast  length 
                        StopSound const s_channelType channel  broadcast     // pass SND_CHANNEL_ANY to stop all sounds
                        SetSoundVolume float volume 
                        UpdateSound
                            GetListenerId const
    idSoundEmitter         GetSoundEmitter const
                        FreeSoundEmitter  immediate 

    // entity binding
    virtual             PreBind
    virtual             PostBind
    virtual             PreUnbind
    virtual             PostUnbind
                        JoinTeam idEntity teammember 
                         idEntity master  orientated 
                        BindToJoint idEntity master const  jointname  orientated 
                        BindToJoint idEntity master jointHandle_t jointnum  orientated 
                        BindToBody idEntity master  bodyId  orientated 
                        Unbind
                        IsBound const
                        IsBoundTo idEntity master  const
    idEntity                 GetBindMaster const
    jointHandle_t            GetBindJoint const
                            GetBindBody const
    idEntity                 GetTeamMaster const
    idEntity                 GetNextTeamEntity const
                        ConvertLocalToWorldTransform idVec3 offset idMat3  
    idVec3                    GetLocalVector const idVec3   const
    idVec3                    GetLocalCoordinates const idVec3   const
    idVec3                    GetWorldVector const idVec3   const
    idVec3                    GetWorldCoordinates const idVec3   const
                        GetMasterPosition idVec3 masterOrigin idMat3 masterAxis  const
                        GetWorldVelocities idVec3 linearVelocity idVec3 angularVelocity  const

    // physics
                            // set a new physics object to be used by this entity
                        SetPhysics idPhysics  
                            // get the physics object used by this entity
    idPhysics                 GetPhysics const
                            // restore physics pointer for save games
                        RestorePhysics idPhysics  
                            // run the physics for this entity
                        RunPhysics
                            // Interpolates the physics, used on MP clients.
                        InterpolatePhysics const float fraction 
                            // InterpolatePhysics actually calls evaluate, this version doesn't.
                        InterpolatePhysicsOnly const float fraction  updateTeam  false 
                            // set the origin of the physics object (relative to bindMaster if not NULL)
                        SetOrigin const idVec3  
                            // set the axis of the physics object (relative to bindMaster if not NULL)
                        SetAxis const idMat3  
                            // use angles to set the axis of the physics object (relative to bindMaster if not NULL)
                        SetAngles const idAngles  
                            // get the floor position underneath the physics object
                        GetFloorPos float max_dist idVec3 floorpos  const
                            // retrieves the transformation going from the physics origin/axis to the visual origin/axis
    virtual             GetPhysicsToVisualTransform idVec3 origin idMat3  
                            // retrieves the transformation going from the physics origin/axis to the sound origin/axis
    virtual             GetPhysicsToSoundTransform idVec3 origin idMat3  
                            // called from the physics object when colliding, should return true if the physics simulation should stop
    virtual             Collide const trace_t collision const idVec3 velocity 
                            // retrieves impact information, 'ent' is the entity retrieving the info
    virtual             GetImpactInfo idEntity    const idVec3 point impactInfo_t  
                            // apply an impulse to the physics object, 'ent' is the entity applying the impulse
    virtual             ApplyImpulse idEntity    const idVec3 point const idVec3 impulse 
                            // add a force to the physics object, 'ent' is the entity adding the force
    virtual             AddForce idEntity    const idVec3 point const idVec3 force 
                            // activate the physics object, 'ent' is the entity activating this entity
    virtual             ActivatePhysics idEntity  
                            // returns true if the physics object is at rest
    virtual             IsAtRest const
                            // returns the time the physics object came to rest
    virtual                 GetRestStartTime const
                            // add a contact entity
    virtual             AddContactEntity idEntity  
                            // remove a touching entity
    virtual             RemoveContactEntity idEntity  

    // damage
                            // returns true if this entity can be damaged from the given origin
    virtual             CanDamage const idVec3 origin idVec3 damagePoint  const
                            // applies damage to this entity
    virtual                Damage idEntity inflictor idEntity attacker const idVec3  const  damageDefName const float damageScale const  location 
                            // adds a damage effect like overlays, blood, sparks, debris etc.
    virtual             AddDamageEffect const trace_t collision const idVec3 velocity const  damageDefName 
                            // callback function for when another entity received damage from this entity.  damage can be adjusted and returned to the caller.
    virtual             DamageFeedback idEntity victim idEntity inflictor  damage 
                            // notifies this entity that it is in pain
    virtual              idEntity inflictor idEntity attacker  damage const idVec3   location 
                            // notifies this entity that is has been killed
    virtual             Killed idEntity inflictor idEntity attacker  damage const idVec3   location 

    // scripting
    virtual             ShouldConstructScriptObjectAtSpawn const
    virtual idThread         ConstructScriptObject
    virtual             DeconstructScriptObject
                        SetSignal signalNum_t signalnum idThread thread const function_t function 
                        ClearSignal idThread thread signalNum_t signalnum 
                        ClearSignalThread signalNum_t signalnum idThread thread 
                        HasSignal signalNum_t signalnum  const
                        Signal signalNum_t signalnum 
                        SignalEvent idThread thread signalNum_t signalnum 

    // gui
                        TriggerGuis
                        HandleGuiCommands idEntity entityGui const   
    virtual             HandleSingleGuiCommand idEntity entityGui idLexer  

    // targets
                        FindTargets
                        RemoveNullTargets
                        ActivateTargets idEntity activator  const

    // misc
    virtual             Teleport const idVec3 origin const idAngles angles idEntity destination 
                        TouchTriggers const
    idCurve_SplineidVec3 GetSpline const
    virtual             ShowEditingDialog

     
        EVENT_STARTSOUNDSHADER
        EVENT_STOPSOUNDSHADER
        EVENT_MAXEVENTS
    

    // Called on clients in an MP game, does the actual interpolation for the entity.
    // This function will eventually replace ClientPredictionThink completely.
    virtual             ClientThink const  curTime const float fraction const  predict 

    virtual             ClientPredictionThink
    virtual             WriteToSnapshot idBitMsg   const
                        ReadFromSnapshot_Ex const idBitMsg  
    virtual             ReadFromSnapshot const idBitMsg  
    virtual             ServerReceiveEvent  event   const idBitMsg  
    virtual             ClientReceiveEvent  event   const idBitMsg  

                        WriteBindToSnapshot idBitMsg   const
                        ReadBindFromSnapshot const idBitMsg  
                        WriteColorToSnapshot idBitMsg   const
                        ReadColorFromSnapshot const idBitMsg  
                        WriteGUIToSnapshot idBitMsg   const
                        ReadGUIFromSnapshot const idBitMsg  

                        ServerSendEvent  eventId const idBitMsg   saveEvent lobbyUserID_t excluding  lobbyUserID_t  const
                        ClientSendEvent  eventId const idBitMsg   const

                        SetUseClientInterpolation     useClientInterpolation   

                        SetSkipReplication const     skipReplication   
                        GetSkipReplication const  return skipReplication 
                        IsReplicated const  return  GetEntityNumber  ENTITYNUM_FIRST_NON_REPLICATED 

                        CreateDeltasFromOldOriginAndAxis const idVec3  oldOrigin const idMat3  oldAxis 
                        DecayOriginAndAxisDelta
    uint32                    GetPredictedKey  return predictionKey 
                        SetPredictedKey uint32    predictionKey   

                        FlagNewSnapshot

    idEntity                GetTeamChain  return teamChain 

    // It is only safe to interpolate if this entity has received two snapshots.
     interpolationBehavior_t 
        USE_NO_INTERPOLATION
        USE_LATEST_SNAP_ONLY
        USE_INTERPOLATION
    

    interpolationBehavior_t GetInterpolationBehavior const  return interpolationBehavior 
    unsigned             GetNumSnapshotsReceived const  return snapshotsReceived 

protected
    renderEntity_t            renderEntity                        // used to present a model to the renderer
                            modelDefHandle                        // handle to static renderer model
    refSound_t                refSound                            // used to present sound to the audio engine

    idVec3                    GetOriginDelta const  return originDelta 
    idMat3                    GetAxisDelta const  return axisDelta 
    
private
    idPhysics_Static        defaultPhysicsObj                    // default physics object
    idPhysics                 physics                            // physics used for this entity
    idEntity                 bindMaster                            // entity bound to if unequal NULL
    jointHandle_t            bindJoint                            // joint bound to if unequal INVALID_JOINT
                            bindBody                            // body bound to if unequal -1
    idEntity                 teamMaster                            // master of the physics team
    idEntity                 teamChain                            // next entity in physics team
                        useClientInterpolation                // disables interpolation for some objects (handy for weapon world models)
                            numPVSAreas                        // number of renderer areas the entity covers
                            PVSAreasMAX_PVS_AREAS            // numbers of the renderer areas the entity covers

    signalList_t             signals

                            mpGUIState                            // local cache to avoid systematic SetStateInt

    uint32                    predictionKey                        // Unique key used to sync predicted ents (projectiles) in MP.

    // Delta values that are set when the server or client disagree on where the render model should be. If this happens,
    // they resolve it through DecayOriginAndAxisDelta()
    idVec3                    originDelta
    idMat3                    axisDelta

    interpolationBehavior_t    interpolationBehavior    
    unsigned             snapshotsReceived

private
                        FixupLocalizedStrings

                        DoDormantTests                // dormant == on the active list, but out of PVS

    // physics
                            // initialize the default physics
                        InitDefaultPhysics const idVec3 origin const idMat3  
                            // update visual position from the physics
                        UpdateFromPhysics  moveBack 
                            // get physics timestep
    virtual                 GetPhysicsTimeStep const

    // entity binding
                        InitBind idEntity master         // initialize an entity binding
                        FinishBind                    // finish an entity binding
                        RemoveBinds                // deletes any entities bound to this object
                        QuitTeam                    // leave the current team

                        UpdatePVSAreas

    // events
                        Event_GetName
                        Event_SetName const   
                        Event_FindTargets
                        Event_ActivateTargets idEntity activator 
                        Event_NumTargets
                        Event_GetTarget float index 
                        Event_RandomTarget const  ignore 
                        Event_Bind idEntity master 
                        Event_BindPosition idEntity master 
                        Event_BindToJoint idEntity master const  jointname float orientated 
                        Event_Unbind
                        Event_RemoveBinds
                        Event_SpawnBind
                        Event_SetOwner idEntity owner 
                        Event_SetModel const  modelname 
                        Event_SetSkin const  skinname 
                        Event_GetShaderParm  parmnum 
                        Event_SetShaderParm  parmnum float value 
                        Event_SetShaderParms float parm0 float parm1 float parm2 float parm3 
                        Event_SetColor float  float green float  
                        Event_GetColor
                        Event_IsHidden
                        Event_Hide
                        Event_Show
                        Event_CacheSoundShader const  soundName 
                        Event_StartSoundShader const  soundName  channel 
                        Event_StopSound  channel  netSync 
                        Event_StartSound const  soundName  channel  netSync 
                        Event_FadeSound  channel float  float  
                        Event_GetWorldOrigin
                        Event_SetWorldOrigin idVec3 const  
                        Event_GetOrigin
                        Event_SetOrigin const idVec3  
                        Event_GetAngles
                        Event_SetAngles const idAngles  
                        Event_SetLinearVelocity const idVec3 velocity 
                        Event_GetLinearVelocity
                        Event_SetAngularVelocity const idVec3 velocity 
                        Event_GetAngularVelocity
                        Event_SetSize const idVec3  const idVec3  
                        Event_GetSize
                        Event_GetMins
                        Event_GetMaxs
                        Event_Touches idEntity  
                        Event_SetGuiParm const   const   
                        Event_SetGuiFloat const   float  
                        Event_GetNextKey const  prefix const  lastMatch 
                        Event_SetKey const   const  value 
                        Event_GetKey const   
                        Event_GetIntKey const   
                        Event_GetFloatKey const   
                        Event_GetVectorKey const   
                        Event_GetEntityKey const   
                        Event_RestorePosition
                        Event_UpdateCameraTarget
                        Event_DistanceTo idEntity  
                        Event_DistanceToPoint const idVec3 point 
                        Event_StartFx const   
                        Event_WaitFrame
                        Event_Wait float  
                        Event_HasFunction const   
                        Event_CallFunction const   
                        Event_SetNeverDormant  enable 
                        Event_SetGui  guiNum const  guiName
                        Event_PrecacheGui const  guiName 
                        Event_GetGuiParm guiNum const  
                        Event_GetGuiParmFloat guiNum const  
                        Event_GuiNamedEvent guiNum const  event
```
