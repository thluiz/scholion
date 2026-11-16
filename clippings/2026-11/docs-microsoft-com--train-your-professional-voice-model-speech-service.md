---
url: "https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/how-to-custom-voice-create-voice"
captured_at: "2026-11-16T03:14:20+00:00"
title: "Train your professional voice model - Speech service - Foundry Tools"
domain: "docs-microsoft-com"
---

In this article, you learn how to fine-tune a professional voice through the Microsoft Foundry portal.

Important

Professional voice fine-tuning is currently only available in some regions. After your voice model is trained in a supported region, you can [copy the professional voice model](#copy-your-voice-model-to-another-project) to a Microsoft Foundry resource in another region as needed. For supported training locations, check the **Custom voice training** column and footnotes in the [Text to speech regions table](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/regions?tabs=tts#regions).

Training duration varies depending on how much data you use. It takes about 10 compute hours on average to fine-tune a professional voice. With a Microsoft Foundry standard (S0) resource, you can train four voices simultaneously. If you reach the limit, wait until at least one of your voice models finishes training, and then try again.

*   [Foundry (new)](#tabpanel_1_foundry-new)
*   [Foundry (classic)](#tabpanel_1_foundry-classic)

On the **Training data** step of **Customize a model**, select one of these training methods:

*   **Neural - HD**: Create an HD voice in the same language as your training data. HD voices are LLM-based and optimized for dynamic conversations. For more information, see [High-definition voices](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/high-definition-voices).
*   **Neural - Default**: Create a voice in the same language as your training data.
*   **Neural - Multi lingual**: Create a voice that speaks multiple languages from single-language training data.
*   **Neural - Multi style**: Create a voice that speaks in multiple styles and emotions.

After you select a method, select a recipe **Version**. The portal evaluates whether your datasets are eligible for that method and version.

To create a custom voice in the Microsoft Foundry portal, follow these steps for one of the following methods:

*   [Foundry (new)](#tabpanel_2_foundry-new)
*   [Foundry (classic)](#tabpanel_2_foundry-classic)

In the new Microsoft Foundry portal, the **Customize a model** page uses a single **Training method** dropdown that covers all variants. These steps continue from the page you opened in [Set up a professional voice](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/professional-voice-create-project), after you upload training data on the **Training data** step.

If you closed the page, [resume your draft customization](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/professional-voice-create-project?tabs=foundry-new&pivots=ai-foundry-portal#resume-an-unfinished-customization) before continuing.

1.  On the **Training data** step, select the **Training method** that matches your scenario. Options include **Neural - HD**, **Neural - Default**, **Neural - Multi lingual**, and **Neural - Multi style**. For details about each method, see [Choose a training method](#choose-a-training-method).
    
2.  Select the training recipe **Version**. The latest version is selected by default. The supported features and training time can vary by version. In some cases, you can choose an earlier version to reduce training time.
    
3.  Confirm the **Model language**.
    
4.  From the **Select dataset** dropdown, select an eligible dataset that you uploaded. The portal evaluates dataset eligibility for the selected training method and version because data-size and duration requirements vary by recipe.
    
    [![Screenshot of the Training data step with Training method, Version, and Select dataset outlined beside the dataset validation summary.](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/media/custom-voice/professional-voice/foundry-new-training-configuration.png)](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/media/custom-voice/professional-voice/foundry-new-training-configuration.png#lightbox)
    
5.  Select **Next**.
    
6.  On the **Review** step, review the basic details, voice talent, training configuration, data size, test information, estimated training time, and cost warning.
    
7.  Select the acknowledgment that training incurs account usage.
    
8.  Select the acknowledgment to agree to the terms of use.
    
9.  Select **Submit** to start training the model.
    

*   [Foundry (new)](#tabpanel_3_foundry-new)
*   [Foundry (classic)](#tabpanel_3_foundry-classic)

1.  Sign in to [Microsoft Foundry](https://ai.azure.com/?cid=learnDocs). Make sure the **New Foundry** toggle is on. These steps refer to **Foundry (new)**.
    
    ![](https://docs.microsoft.com/en-us/azure/foundry/media/version-banner/new-foundry.png)
    
2.  Select **Build** from the upper-right menu.
    
3.  Select **Services** in the left pane.
    
4.  Select the **Customizations** tab to view your Professional Voice customization jobs and their status.
    
    [![Screenshot of a succeeded Professional Voice customization job in the new Foundry portal.](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/media/custom-voice/professional-voice/foundry-new-customizations-status.png)](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/media/custom-voice/professional-voice/foundry-new-customizations-status.png#lightbox)
    
5.  To stop a model that's still training, select its name, and then select **Cancel training**. You aren't charged for canceled training.
    
6.  After the status changes to **Succeeded**, select the model name to open its **Details** page. The page displays the training and deployment status, task parameters, model attributes, training data, engine version, creation time, and model ID.
    

If training fails, review the reported error before starting another job. For data-related errors, [review your dataset's validation results](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/professional-voice-create-training-set?tabs=foundry-new&pivots=ai-foundry-portal#review-data-issues) and correct the affected recordings or transcripts. If you can't resolve the failure, [contact support](https://docs.microsoft.com/en-us/azure/ai-services/cognitive-services-support-options).

Azure text to speech engines are updated from time to time to capture the latest language model that defines the pronunciation of the language. After you train your voice, you can apply your voice to the new language model by updating to the latest engine version.

*   [Foundry (new)](#tabpanel_4_foundry-new)
*   [Foundry (classic)](#tabpanel_4_foundry-classic)

1.  Select **Build** > **Services** > **Customizations**.
2.  Select the name of the Professional Voice model.
3.  When the model details page indicates that a new engine is available, select **Install the latest engine**.
4.  In the **Install the latest engine** dialog, select **Confirm**. The update creates a new engine version at no extra cost and keeps the existing versions.

The new engine version becomes the default version. To use another installed version as the default, select the **Engine version** value on the model details page, select the version, and then select **Done**.

[![Screenshot of the Engine version dialog in the new Foundry portal.](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/media/custom-voice/professional-voice/foundry-new-engine-version.png)](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/media/custom-voice/professional-voice/foundry-new-engine-version.png#lightbox)

Updating the engine creates a new version of the model at no extra cost. After you update the engine version for your voice model, you need to deploy the new version to [create a new endpoint](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/professional-voice-deploy-endpoint#add-a-deployment-endpoint). You can only deploy the default version.

After you create a new endpoint, you need to [transfer the traffic to the new endpoint in your product](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/professional-voice-deploy-endpoint#switch-to-a-new-voice-model-in-your-product).

To learn more about the capabilities and limits of this feature, and the best practice to improve your model quality, see [Characteristics and limitations for using custom voice](https://docs.microsoft.com/en-us/azure/ai-foundry/responsible-ai/speech-service/text-to-speech/transparency-note).

*   [Foundry (new)](#tabpanel_5_foundry-new)
*   [Foundry (classic)](#tabpanel_5_foundry-classic)

After training, you can copy your voice model to another Microsoft Foundry project in the same region or another region. For example, you can train a Professional Voice model in a [supported training region](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/regions?tabs=tts#regions) and copy it to a Foundry resource and project in another region.

1.  Select **Build** > **Services** > **Customizations**.
    
2.  Select the row for the model that you want to copy. In the model details pane, select **Copy to**.
    
    [![Screenshot of the Customizations model list and model details pane, with the selected model name and Copy to action outlined.](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/media/custom-voice/professional-voice/foundry-new-model-actions.png)](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/media/custom-voice/professional-voice/foundry-new-model-actions.png#lightbox)
    
3.  In the **Copy speech model** dialog, select the **Subscription**, **Resource group**, **Target foundry resource**, and **Target foundry project**.
    
    [![Screenshot of the Copy speech model dialog in the new Foundry portal.](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/media/custom-voice/professional-voice/foundry-new-copy-model.png)](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/media/custom-voice/professional-voice/foundry-new-copy-model.png#lightbox)
    
4.  Select **Copy**. The copied model appears in the target project's **Customizations** list after the copy operation finishes.
    

In this article, you learn how to fine-tune a professional voice through the Speech Studio portal.

Important

Professional voice fine-tuning is currently only available in some regions. After your voice model is trained in a supported region, you can [copy](#copy-your-voice-model-to-another-project) it to a Foundry resource for Speech in another region as needed. For more information, see the footnotes in the [Speech service table](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/regions#regions).

Training duration varies depending on how much data you use. It takes about 10 compute hours on average to fine-tune a professional voice. Standard subscription (S0) users can train four voices simultaneously. If you reach the limit, wait until at least one of your voice models finishes training, and then try again.

After you validate your data files, use them to build your custom voice model. When you create a custom voice, you can choose to train it with one of the following methods:

*   [Neural - HD Voice](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/how-to-custom-voice-create-voice?tabs=hdvoice#train-your-custom-voice-model): Create a HD voice in the same language of your training data. Azure neural HD voices are LLM-based, optimized for dynamic conversations. Learn more about neural HD voices [here](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/high-definition-voices).
    
*   [Neural](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/how-to-custom-voice-create-voice?tabs=neural#train-your-custom-voice-model): Create a voice in the same language as your training data.
    
*   [Neural - multilingual](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/how-to-custom-voice-create-voice?tabs=multilingual#train-your-custom-voice-model): Create a voice that speaks multiple languages using the single-language training data. For example, with the `en-US` primary training data, you can create a voice that speaks `en-US`, `de-DE`, `zh-CN` etc. secondary languages.
    
    The primary language of the training data and the secondary languages must be in the [languages that are supported](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support?tabs=tts#professional-voice) for multilingual voice training. You don't need to prepare training data in the secondary languages.
    
*   [Neural - multi style](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/how-to-custom-voice-create-voice?tabs=multistyle#train-your-custom-voice-model): Create a custom voice that speaks in multiple styles and emotions, without adding new training data. Multiple style voices are useful for video game characters, conversational chatbots, audiobooks, content readers, and more.
    
    To create a multiple style voice, you need to prepare a set of general training data, at least 300 utterances. Select one or more of the preset target speaking styles. You can also create multiple custom styles by providing style samples, of at least 100 utterances per style, as extra training data for the same voice. The supported preset styles vary according to different languages. See [available preset styles across different languages](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/how-to-custom-voice-create-voice?tabs=multistyle#available-preset-styles-across-different-languages).
    
*   [Neural - cross lingual](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/how-to-custom-voice-create-voice?tabs=crosslingual#train-your-custom-voice-model): Create a voice that speaks a different language from your training data. For example, with the `zh-CN` training data, you can create a voice that speaks `en-US`.
    
    The language of the training data and the target language must both be one of the [languages that are supported](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support?tabs=tts#professional-voice) for cross lingual voice training. You don't need to prepare training data in the target language, but your test script must be in the target language.
    
    Note
    
    Neural - cross lingual retires on August 25, 2026. The voice models you already created by using these retired methods aren't affected.
    

The language of the training data must be one of the [languages that are supported](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support?tabs=tts) for custom voice, cross-lingual, or multiple style training.

To create a custom voice in Speech Studio, follow these steps for one of the following methods:

*   [Neural - HD Voice](#tabpanel_1_hdvoice)
*   [Neural](#tabpanel_1_neural)
*   [Neural - multilingual](#tabpanel_1_multilingual)
*   [Neural - multi style](#tabpanel_1_multistyle)
*   [Neural - cross lingual](#tabpanel_1_crosslingual)

1.  Sign in to the [Speech Studio](https://aka.ms/speechstudio/customvoice).
    
2.  Select **Custom voice** > _<Your project name>_ > **Train model** > **Train a new model**.
    
3.  Select **Neural - HD Voice** as the [training method](#choose-a-training-method) for your model. To use a different training method, see [Neural](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/how-to-custom-voice-create-voice?tabs=neural#train-your-custom-voice-model), [Neural - cross lingual](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/how-to-custom-voice-create-voice?tabs=crosslingual#train-your-custom-voice-model), [Neural - multi style](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/how-to-custom-voice-create-voice?tabs=multistyle#train-your-custom-voice-model), or [Neural - multilingual](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/how-to-custom-voice-create-voice?tabs=multilingual#train-your-custom-voice-model).
    
    ![Screenshot that shows how to select neural HD voice training.](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/media/custom-voice/cnv-train-neural-hd-voice.png)
    
    Note
    
    HD voices are only available in regions that support _High performance_ type. For information about regions where the _High performance_ endpoint type is supported, see the _Custom voice high performance endpoint_ column in the _Text to speech_ tab of the [regions](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/regions#regions) table.
    
4.  Select the data that you want to use for training. Duplicate audio names are removed from the training. Make sure that the data you select doesn't contain the same audio names across multiple _.zip_ files.
    
    You can select only successfully processed datasets for training. Check your data processing status if you don't see your training set in the list. Prefer to select training data processed as **Contextual**.
    
5.  Select a speaker file with the voice talent statement that corresponds to the speaker in your training data.
    
6.  Select **Next**.
    
7.  Each training process automatically generates 100 primary language sample audio files to help you test the model with a default script.
    

Optionally, you can also select **Add my own test script** and provide your own test script with up to 100 utterances to test the default style at no extra cost. The generated audio files are a combination of the automatic test scripts and custom test scripts. For more information, see [test script requirements](#test-script-requirements).

1.  Enter a **Name** to help you identify the model. Choose a name carefully. The model name is used as the voice name in your [speech synthesis request](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/professional-voice-deploy-endpoint#use-your-custom-voice) by the SDK and SSML input. Only letters, numbers, and a few punctuation characters are allowed. Use different names for different neural voice models. The Dragon HD suffix is automatically added to your model name.
2.  Optionally, enter the **Description** to help you identify the model. A common use of the description is to record the names of the data that you used to create the model.
3.  Select **Next**.
4.  Review the settings and select the box to accept the terms of use.
5.  Select **Submit** to start training the model.

The **Train model** table displays a new entry that corresponds to this newly created model. The status reflects the process of converting your data to a voice model, as described in this table:

State

Meaning

Processing

Your voice model is being created.

Succeeded

Your voice model has been created and can be deployed.

Failed

Your voice model has failed in training. The cause of the failure might be, for example, unseen data problems or network issues.

Canceled

The training for your voice model was canceled.

While the model status is **Processing**, you can select **Cancel training** to cancel your voice model. You're not charged for this canceled training.

![Screenshot that shows how to cancel training for a model.](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/media/custom-voice/cnv-cancel-training.png)

After you finish training the model successfully, you can review the model details and [Test your voice model](#test-your-voice-model).

You can use the [Audio Content Creation](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/how-to-audio-content-creation) tool in Speech Studio to create audio and fine-tune your deployed voice. If applicable for your voice, you can select one of multiple styles.

1.  If you want to rename the model you built, select **Clone model** to create a clone of the model with a new name in the current project.
    
    ![Screenshot of selecting the Clone model button.](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/media/custom-voice/cnv-clone-model.png)
    
2.  Enter the new name on the **Clone voice model** window, then select **Submit**. The text _Neural_ is automatically added as a suffix to your new model name.
    
    ![Screenshot of cloning a model with a new name.](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/media/custom-voice/cnv-clone-model-rename.png)
    

After your voice model is successfully built, you can use the generated sample audio files to test it before you deploy it.

The quality of the voice depends on many factors, such as:

*   The size of the training data.
*   The quality of the recording.
*   The accuracy of the transcript file.
*   How well the recorded voice in the training data matches the personality of the designed voice for your intended use case.

Select **DefaultTests** under **Testing** to listen to the sample audio files. The default test samples include 100 sample audio files generated automatically during training to help you test the model. In addition to these 100 audio files provided by default, your own test script utterances are also added to **DefaultTests** set. This addition is at most 100 utterances. You're not charged for the testing with **DefaultTests**.

![Screenshot of selecting DefaultTests under Testing.](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/media/custom-voice/cnv-model-default-test.png)

If you want to upload your own test scripts to further test your model, select **Add test scripts** to upload your own test script.

![Screenshot of adding model test scripts.](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/media/custom-voice/cnv-model-add-testscripts.png)

Before you upload test script, check the [Test script requirements](#test-script-requirements). You're charged for the extra testing with the batch synthesis based on the number of billable characters. See [Azure Speech in Foundry Tools pricing](https://azure.microsoft.com/pricing/details/cognitive-services/speech-services/).

Under **Add test scripts**, select **Browse for a file** to select your own script, then select **Add** to upload it.

![Screenshot of uploading model test scripts.](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/media/custom-voice/cnv-model-upload-testscripts.png)

The test script must be a _.txt_ file that is less than 1 MB. Supported encoding formats include ANSI/ASCII, UTF-8, UTF-8-BOM, UTF-16-LE, or UTF-16-BE.

Unlike the [training transcription files](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/how-to-custom-voice-training-data#transcription-data-for-individual-utterances-and-matching-transcript), the test script should exclude the utterance ID, which is the filename of each utterance. Otherwise, these IDs are spoken.

Here's an example set of utterances in one _.txt_ file:

```
This is the waistline, and it's falling.
We have trouble scoring.
It was Janet Maslin.
```

Each paragraph of the utterance results in a separate audio. If you want to combine all sentences into one audio, make them a single paragraph.

Note

The generated audio files are a combination of the automatic test scripts and custom test scripts.

Azure text to speech engines are updated from time to time to capture the latest language model that defines the pronunciation of the language. After you train your voice, you can apply your voice to the new language model by updating to the latest engine version.

1.  When a new engine is available, you're prompted to update your neural voice model.
    
    [![Screenshot of displaying engine update message.](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/media/custom-voice/cnv-engine-update-prompt.png)](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/media/custom-voice/cnv-engine-update-prompt.png#lightbox)
    
2.  Go to the model details page and follow the on-screen instructions to install the latest engine.
    
    ![Screenshot of following on-screen instructions to install the new engine.](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/media/custom-voice/cnv-new-engine-install.png)
    
    Alternatively, select **Install the latest engine** later to update your model to the latest engine version.
    
    ![Screenshot of selecting Install the latest engine button to update engine.](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/media/custom-voice/cnv-install-latest-engine.png)
    
    You're not charged for engine update. The previous versions are still kept.
    
3.  You can check all engine versions for the model from the **Engine version** list, or remove one if you don't need it anymore.
    
    ![Screenshot of displaying Engine version drop-down list.](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/media/custom-voice/cnv-engine-version.png)
    
    The updated version is automatically set as default. But you can change the default version by selecting a version from the drop-down list and selecting **Set as default**.
    
    ![Screenshot that shows how to set a version as default.](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/media/custom-voice/cnv-engine-set-default.png)
    

If you want to test each engine version of your voice model, you can select a version from the list, then select **DefaultTests** under **Testing** to listen to the sample audio files. If you want to upload your own test scripts to further test your current engine version, first make sure the version is set as default, then follow the steps in [Test your voice model](#test-your-voice-model).

Updating the engine creates a new version of the model at no extra cost. After you update the engine version for your voice model, you need to deploy the new version to [create a new endpoint](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/professional-voice-deploy-endpoint#add-a-deployment-endpoint). You can only deploy the default version.

![Screenshot that shows how to redeploy a new version of your voice model.](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/media/custom-voice/cnv-engine-redeploy.png)

After you create a new endpoint, you need to [transfer the traffic to the new endpoint in your product](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/professional-voice-deploy-endpoint#switch-to-a-new-voice-model-in-your-product).

To learn more about the capabilities and limits of this feature, and the best practice to improve your model quality, see [Characteristics and limitations for using custom voice](https://docs.microsoft.com/en-us/azure/ai-foundry/responsible-ai/speech-service/text-to-speech/transparency-note).

You can copy your voice model to another project for the same region or another region. For example, you can copy a neural voice model that was trained in one region, to a project for another region.

Note

Professional voice fine-tuning is currently only available in some regions. You can copy a neural voice model from those regions to other regions. For more information, see the [regions for custom voice](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/regions#regions).

To copy your custom voice model to another project:

1.  On the **Train model** tab, select a voice model that you want to copy, and then select **Copy to project**.
    
    ![Screenshot of the copy to project option.](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/media/custom-voice/cnv-model-copy.png)
    
2.  Select the **Subscription**, **Region**, **Speech resource**, and **Project** where you want to copy the model. You must have a speech resource and project in the target region, otherwise you need to create them first.
    
    ![Screenshot of the copy voice model dialog.](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/media/custom-voice/cnv-model-copy-dialog.png)
    
3.  Select **Submit** to copy the model.
    
4.  Select **View model** under the notification message for the successful copying.
    

Navigate to the project where you copied the model to [deploy the model copy](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/professional-voice-deploy-endpoint).

In this article, you learn how to fine-tune a professional voice through the custom voice API.

Important

Professional voice fine-tuning is currently only available in some regions. After your voice model is trained in a supported region, you can copy it to a Foundry resource in another region as needed. For more information, see the footnotes in the [Speech service table](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/regions#regions).

Training duration varies depending on how much data you use. It takes about 10 compute hours on average to fine-tune a professional voice. Standard subscription (S0) users can train four voices simultaneously. If you reach the limit, wait until at least one of your voice models finishes training, and then try again.

After you validate your data files, use them to build your custom voice model. When you create a custom voice, you can choose to train it with one of the following methods:

*   [Neural - HD Voice](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/how-to-custom-voice-create-voice?tabs=hdvoice#create-a-voice-model): Create a HD voice in the same language of your training data. Azure neural HD voices are LLM-based, optimized for dynamic conversations. Learn more about neural HD voices [here](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/high-definition-voices).
    
*   [Neural](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/how-to-custom-voice-create-voice?tabs=neural#create-a-voice-model): Create a voice in the same language as your training data.
    
*   [Neural - multi style](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/how-to-custom-voice-create-voice?tabs=multistyle#create-a-voice-model): Create a custom voice that speaks in multiple styles and emotions, without adding new training data. Multiple style voices are useful for video game characters, conversational chatbots, audiobooks, content readers, and more.
    
    To create a multiple style voice, you need to prepare a set of general training data, at least 300 utterances. Select one or more of the preset target speaking styles. You can also create multiple custom styles by providing style samples, of at least 100 utterances per style, as extra training data for the same voice. The supported preset styles vary according to different languages. See [available preset styles across different languages](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/how-to-custom-voice-create-voice?tabs=multistyle#available-preset-styles-across-different-languages).
    
*   [Neural - cross lingual](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/how-to-custom-voice-create-voice?tabs=crosslingual#create-a-voice-model): Create a voice that speaks a different language from your training data. For example, with the `fr-FR` training data, you can create a voice that speaks `en-US`.
    
    The language of the training data and the target language must both be one of the [languages that are supported](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support?tabs=tts#professional-voice) for cross lingual voice training. You don't need to prepare training data in the target language, but your test script must be in the target language.
    
    Note
    
    Neural - cross lingual retires on August 25, 2026. The voice models you already created by using these retired methods aren't affected.
    

The language of the training data must be one of the [languages that are supported](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support?tabs=tts) for custom voice, cross lingual, or multiple style or HD voice training.

*   [Neural - HD Voice](#tabpanel_1_hdvoice)
*   [Neural](#tabpanel_1_neural)
*   [Neural - multi style](#tabpanel_1_multistyle)
*   [Neural - cross lingual](#tabpanel_1_crosslingual)
*   [Neural - multi lingual](#tabpanel_1_multilingual)

To create an HD voice, use the [Models\_Create](https://docs.microsoft.com/en-us/rest/api/aiservices/speechapi/models/create) operation of the custom voice API. Construct the request body according to the following instructions:

*   Set the required `projectId` property. See [create a project](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/professional-voice-create-project).
*   Set the required `consentId` property. See [add voice talent consent](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/professional-voice-create-consent).
*   Set the required `trainingSetId` property. See [create a training set](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/professional-voice-create-training-set).
*   Set the required recipe `kind` property to `HD` for neural voice training. The recipe kind indicates the training method and can't be changed later. To use a different training method, see [Neural](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/how-to-custom-voice-create-voice?tabs=neural#create-a-voice-model), [Neural - cross lingual](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/how-to-custom-voice-create-voice?tabs=crosslingual#create-a-voice-model), or [Neural - multi style](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/how-to-custom-voice-create-voice?tabs=multistyle#create-a-voice-model). See [Bilingual training](#bilingual-training) for more information about bilingual training and differences between locales.
*   Set the required `voiceName` property. The voice name automatically adds the Dragon HD suffix and can't be changed later. Choose a name carefully. The SDK and SSML input use the voice name in your [speech synthesis request](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/professional-voice-deploy-endpoint#use-your-custom-voice). Only letters, numbers, and a few punctuation characters are allowed before the specific suffix. Use different names for different neural voice models.
*   Optionally, set the `description` property for the voice description. The voice description can be changed later.

Make an HTTP PUT request using the URI as shown in the following [Models\_Create](https://docs.microsoft.com/en-us/rest/api/aiservices/speechapi/models/create) example.

*   Replace `YourResourceKey` with your Speech resource key.
*   Replace `YourResourceName` with your Speech resource name.
*   Replace `JessicaModelId` with a model ID of your choice. The case sensitive ID will be used in the model's URI and can't be changed later.

```
curl -v -X PUT -H "Ocp-Apim-Subscription-Key: YourResourceKey" -H "Content-Type: application/json" -d '{
  "voiceName": "Jessica",
  "description": "Jessica HD voice",
  "recipe": {
    "kind": "HD"
  },
  "projectId": "ProjectId",
  "consentId": "JessicaConsentId",
  "trainingSetId": "JessicaTrainingSetId"
} '  "https://YourResourceName.cognitiveservices.azure.com/customvoice/models/JessicaModelId?api-version=2026-01-01"
```

You should receive a response body in the following format:

```
{
  "id": "JessicaModelId",
  "voiceName": "Jessica:DragonHDLatestNeural",
  "description": "Jessica HD voice",
  "recipe": {
    "kind": "HD",
    "version": "V1.0"
  },
  "projectId": "ProjectId",
  "consentId": "JessicaConsentId",
  "trainingSetId": "JessicaTrainingSetId",
  "locale": "en-US",
  "engineVersion": "2023.07.04.0",
  "status": "NotStarted",
  "createdDateTime": "2023-04-01T05:30:00.000Z",
  "lastActionDateTime": "2023-04-02T10:15:30.000Z"
}
```

If you select the **Neural** training type, you can train a voice to speak in multiple languages. The `zh-CN`, `zh-HK`, and `zh-TW` locales support bilingual training for the voice to speak both Chinese and English. Depending in part on your training data, the synthesized voice can speak English with an English native accent or English with the same accent as the training data.

Note

To enable a voice in the Chinese locale to speak English with the same accent as the sample data, upload English data that includes at least 100 sentences or 10 minutes of English content and doesn't exceed the amount of Chinese content.

The following table summarizes the different preset styles according to different languages.

Speaking style

Language (locale)

angry

English (United States) (`en-US`)  
Japanese (Japan) (`ja-JP`) 1  
Chinese (Mandarin, Simplified) (`zh-CN`) 1

calm

Chinese (Mandarin, Simplified) (`zh-CN`) 1

chat

Chinese (Mandarin, Simplified) (`zh-CN`) 1

cheerful

English (United States) (`en-US`)  
Japanese (Japan) (`ja-JP`) 1  
Chinese (Mandarin, Simplified) (`zh-CN`) 1

disgruntled

Chinese (Mandarin, Simplified) (`zh-CN`) 1

excited

English (United States) (`en-US`)

fearful

Chinese (Mandarin, Simplified) (`zh-CN`) 1

friendly

English (United States) (`en-US`)

hopeful

English (United States) (`en-US`)

sad

English (United States) (`en-US`)  
Japanese (Japan) (`ja-JP`) 1  
Chinese (Mandarin, Simplified) (`zh-CN`) 1

shouting

English (United States) (`en-US`)

serious

Chinese (Mandarin, Simplified) (`zh-CN`) 1

terrified

English (United States) (`en-US`)

unfriendly

English (United States) (`en-US`)

whispering

English (United States) (`en-US`)

1 The neural voice style is available in public preview. For the current list of regions that support styles in public preview, see the [Speech service regions table](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/regions?tabs=tts).

* * *

To get the training status of a voice model, use the [Models\_Get](https://docs.microsoft.com/en-us/rest/api/aiservices/speechapi/models/get) operation of the custom voice API. Construct the request URI according to the following instructions:

Make an HTTP GET request using the URI as shown in the following [Models\_Get](https://docs.microsoft.com/en-us/rest/api/aiservices/speechapi/models/get) example.

*   Replace `YourResourceKey` with your Speech resource key.
*   Replace `YourResourceName` with your Speech resource name.
*   Replace `JessicaModelId` if you specified a different model ID in the previous step.

```
curl -v -X GET "https://YourResourceName.cognitiveservices.azure.com/customvoice/models/JessicaModelId?api-version=2026-01-01" -H "Ocp-Apim-Subscription-Key: YourResourceKey"
```

You should receive a response body in the following format.

Note

The recipe `kind` and other properties depend on how you [trained the voice](#choose-a-training-method). In this example, the recipe kind is `Default` for neural voice training.

```
{
  "id": "JessicaModelId",
  "voiceName": "Jessica",
  "description": "Jessica voice",
  "recipe": {
    "kind": "Default",
    "version": "V9.0"
  },
  "projectId": "ProjectId",
  "consentId": "JessicaConsentId",
  "trainingSetId": "JessicaTrainingSetId",
  "locale": "en-US",
  "engineVersion": "2023.07.04.0",
  "status": "Succeeded",
  "createdDateTime": "2023-04-01T05:30:00.000Z",
  "lastActionDateTime": "2023-04-02T10:15:30.000Z"
}
```

You might need to wait for several minutes before the training is completed. Eventually the status will change to either `Succeeded` or `Failed`.
