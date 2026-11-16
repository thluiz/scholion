---
title: "Train your professional voice model - Speech service - Foundry Tools"
date: '2020-07-05T14:11:24+00:00'
category: webclip
summary: 'The article explains how to fine-tune a professional voice in Foundry, Speech Studio, or the custom voice API, including training methods, region limits, model updates, copying, and deployment.'
tags: ["professional-voice", "speech-service", "foundry", "custom-voice"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Train your professional voice model - Speech service - Foundry Tools"
    url: "https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/how-to-custom-voice-create-voice"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/docs-microsoft-com--train-your-professional-voice-model-speech-service.md"
    kind: repo
---

The page describes how to fine-tune a professional voice and where that workflow is available. It notes that support is limited to some regions, training time depends on data size, and S0 resources can train four voices at once. It also explains the available training methods, how the portal checks dataset eligibility, and how to start, cancel, and review training jobs.

## Reading notes

- Professional voice fine-tuning is only available in some regions, and trained models can be copied to another project or region when needed.
- Training usually takes about 10 compute hours on average, and an S0 resource can train four voices simultaneously.
- The portal offers Neural - HD, Neural - Default, Neural - Multi lingual, and Neural - Multi style training methods, with recipe versions that affect features and training time.
- In Foundry, the workflow runs through Customize a model, where you choose the method, version, model language, and eligible dataset before submitting training.
- The model details page shows training and deployment status, task parameters, model attributes, data, engine version, creation time, and model ID.
- If training fails, the page tells you to review the error, check dataset validation results for data issues, or contact support.
- The article says Azure text to speech engines are updated over time, and a new engine version can be installed at no extra cost.
- Updating the engine creates a new model version, keeps previous versions, and requires deploying the new default version before creating a new endpoint.
- A trained voice model can be copied to another project in the same region or a different region through the portal or copied through the model workflow.
- In Speech Studio and the custom voice API, the page describes Neural - HD Voice, Neural, Neural - multilingual, Neural - multi style, and Neural - cross lingual training options.
- Neural - cross lingual retires on August 25, 2026, and existing models created with it are not affected.
- For Neural - multi style, the page says you need at least 300 utterances of general training data, plus style samples of at least 100 utterances per custom style if you add your own styles.
- For cross-lingual training, the training data and target language must both be supported, and the test script must be in the target language.
- The API section shows required request fields such as projectId, consentId, trainingSetId, recipe kind, voiceName, and optional description, plus example GET and PUT requests.
