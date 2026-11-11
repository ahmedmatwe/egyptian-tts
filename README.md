# Egyptian-TTS — صوت مصري عامي محلي

موديل **NAMAA-Egyptian-TTS** (مبني على Chatterbox Multilingual). رخصة **MIT**: الاستخدام التجاري مسموح مع ذكر الاسم.
بيشتغل على الماك (MPS) أو أي جهاز من غير كارت شاشة (CPU)، مجاني ومن غير حدود.

## الاستخدام
```bash
~/Desktop/Egyptian-TTS/speak.sh "يا معلم سيد! أنا جبتلك اختراع" out.wav
~/Desktop/Egyptian-TTS/speak.sh "حتى اللي في دماغي؟!" out.wav voice_ref.wav --exaggeration 0.7
```
- `reference.wav` اختياري: عينة 5–10 ثواني للنبرة. **متستخدمش صوت شخص حقيقي من غير إذنه.**
- `--exaggeration` (0.3–1.0): قد إيه الأداء معبّر. `--seed`: غيّره عشان تاخد أداء مختلف.
- الإخراج WAV بجودة 24kHz. فيه علامة مائية مخفية (Perth) من Chatterbox، مبتسمعش.

## المحتويات
- `venv/` بيئة Python 3.11 جاهزة · `hf-cache/` الموديلات (~5GB) · `tts.py` الكود · `speak.sh` أمر التشغيل.

## ذكر المصدر
الصوت: NAMAA-Egyptian-TTS (NAMAA Community) على Chatterbox (Resemble AI)، رخصة MIT.

## على GitHub (من غير الماك)
الريبو ده public عشان GitHub Actions يبقى مجاني من غير حد دقايق.
- يدوي: Actions → speak → Run workflow، أو: `gh workflow run speak -R ahmedmatwe/egyptian-tts -f text="..." -f request_id=ep1`
- من مشروع تاني: `repository_dispatch` بنوع `speak` و `client_payload: {text, request_id, exaggeration, seed}`، وبعدين حمّل الـ artifact `speech-<request_id>` وامسحه.
- ملفات الصوت بتتمسح لوحدها بعد يوم، والمشاريع بتمسحها أول ما تاخدها.
