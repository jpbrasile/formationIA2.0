# Guide de référence rapide pour LocalAI

## Génération de texte (GPT)

LocalAI prend en charge la génération de texte avec GPT à l'aide de llama.cpp et d'autres backends. Pour générer une complétion de chat, vous pouvez envoyer une requête POST à l'API de chat[1].

```bash
curl http://localhost:8080/v1/chat/completions -H "Content-Type: application/json" -d '{ "model": "TheBloke/WizardLM-13B-V1.2-GGML/wizardlm-13b-v1.2.ggmlv3.q2_K.bin", "messages": [{"role": "user", "content": "Dites que c'est un test!"}]'
```

## Génération d'images

LocalAI prend en charge la génération d'images avec Stable diffusion, fonctionnant sur CPU en utilisant une implémentation C++. Pour générer une image, vous pouvez envoyer une requête POST à l'endpoint /v1/images/generations[2].

```bash
curl http://localhost:8080/v1/images/generations -H "Content-Type: application/json" -d '{ "prompt": "un paysage de montagne enneigée", "size": "512x512" }'
```

## Reconnaissance vocale

LocalAI peut être utilisé pour la reconnaissance vocale automatique (ASR), comme décrit dans un projet sur Hackaday[3]. Bien que les détails spécifiques de la mise en œuvre de l'ASR avec LocalAI ne soient pas clairement indiqués dans les résultats de recherche, il est mentionné que LocalAI fournit un guide étape par étape pour la configuration.

## Traduction

LocalAI prend en charge la traduction en utilisant des modèles OpenNMT open source. Les détails spécifiques de l'utilisation de la fonctionnalité de traduction de LocalAI ne sont pas clairement indiqués dans les résultats de recherche[4].

## Autres fonctionnalités

LocalAI prend également en charge d'autres fonctionnalités, telles que la génération audio à partir de texte et la possibilité d'exécuter une multitude de modèles localement[8][9].
```

Veuillez noter que ce guide de référence rapide est basé sur les informations disponibles dans les résultats de recherche et peut ne pas couvrir toutes les fonctionnalités de LocalAI. Pour une documentation plus détaillée, veuillez consulter le site web de LocalAI et sa documentation officielle.

Citations:
[1] https://localai.io/features/text-generation/
[2] https://localai.io/features/image-generation/
[3] https://hackaday.io/project/193635-automatic-speech-recognition-ai-assistant
[4] https://help.nextcloud.com/t/ai-in-nextcloud-what-why-and-how/166916
[5] https://localai.io/docs/advanced/fine-tuning/
[6] https://localai.io/basics/getting_started/
[7] https://cloud.google.com/blog/products/ai-machine-learning/speech-on-device-run-server-quality-speech-ai-locally
[8] https://localai.io/integrations/mods/
[9] https://www.reddit.com/r/selfhosted/comments/14llh77/update_localai_v1200_is_here_with_texttoaudio_and/?rdt=42215
[10] https://github.com/go-skynet/LocalAI/issues/921
[11] https://deepgram.com/ai-apps/local-ai
[12] https://github.com/ggerganov/llama.cpp/discussions/1201
[13] https://semaphoreci.com/blog/localai
[14] https://llmstack.ai/docs/processors/localai
[15] https://nextcloud.com/blog/ai-in-nextcloud-what-why-and-how/
[16] https://chatgpt.ai/sites/localai/
[17] https://github.com/mudler/LocalAI/issues/1042
[18] https://github.com/mudler/LocalAI
[19] https://www.reddit.com/r/selfhosted/comments/157kumd/localai_v1220_is_out/?rdt=48886
[20] https://docs.dify.ai/advanced/model-configuration/localai
[21] https://topai.tools/s/local-image-generator
[22] https://www.lesswrong.com/posts/SsTzdyaCqqyxanp3C/how-did-you-integrate-voice-to-text-ai-into-your-workflow
[23] https://www.youtube.com/watch?v=Xh57mMlfuMk
[24] https://hackaday.io/project/193635/log/225199
[25] https://worldoscar.org/knowledge-base/local-ai-scribe-setup/
