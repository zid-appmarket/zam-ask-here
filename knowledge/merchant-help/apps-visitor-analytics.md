---
# Synced from https://help.zid.sa/ar/apps/visitor-analytics
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: mh-apps-visitor-analytics
title: "ربط Clarity وHotjar وCrazy Egg وContentsquare وSmartarget بمتجرك في زد"
product: zam
audience: all
status: verified
updated: 2026-10-26
source_url: https://help.zid.sa/ar/apps/visitor-analytics
tags: [from-docs-site, merchant-help-center]
language: ar
---

> سجّل جلسات الزوار وخرائطهم الحرارية بأداة Microsoft Clarity أو Hotjar أو Crazy Egg أو Contentsquare، وأضف أدوات Smartarget، برمز كل أداة.
# ربط Clarity وHotjar وCrazy Egg وContentsquare وSmartarget بمتجرك في زد

تسجّل أدوات تحليل الزوار تنقّل المتسوقين في متجرك: أين يضغطون، وإلى أي حد يمررون الصفحة، وأين يغادرون قبل الشراء. وتكشف لك تسجيلات الجلسات والخرائط الحرارية ما ينبغي إصلاحه في صفحة المنتج أو صفحة الدفع. أما Smartarget فيضيف إلى واجهة متجرك أدوات تفاعلية، كالقصص والتقييمات وأزرار التواصل.

لكل أداة تطبيق مجاني في سوق التطبيقات ، وأغلبها في تصنيف **التحليلات والتقارير**، وتربطها جميعًا بطريقة واحدة: أنشئ حسابًا في الأداة، وانسخ الرمز الذي تعطيك إياه، والصقه في حقل **رمز الحساب** في التطبيق. وتدفع للأداة نفسها مقابل خططها المدفوعة إن وُجدت.

التطبيق ما يقدمه الرمز الذي تُدخله

**مايكروسوفت كلاريتي** تسجيلات جلسات وخرائط حرارية ورؤى بالذكاء الاصطناعي مجانًا من Microsoft معرّف مشروعك في Clarity

**Hotjar** تسجيلات الجلسات والخرائط الحرارية وآراء الزوار، لتفهم سلوك عملائك معرّف موقعك في Hotjar

**Crazyegg** خرائط حرارية وخرائط تمرير ومصادر الزيارات لكل نقرة وتسجيلات الجلسات رقم حسابك، مثل `1234/5678`

**كونتنت سكوير** رحلة الزائر كاملة وخرائط حرارية وإعادة تشغيل الجلسات دون وسوم يدوية المعرّف الوارد في وسم Contentsquare

**Smartarget** أدوات تفاعلية للزوار، كالقصص والتقييمات وأشرطة الزاوية معرّف المستخدم في Smartarget

## تفعيل التطبيق في زد

- افتح **التطبيقات** > **سوق التطبيقات** في لوحة تحكم زد، وابحث باسم الأداة.

- افتح صفحة التطبيق واضغط **تفعيل**، فتنتقل إلى بطاقة **تفعيل التطبيق**.

- الصق الرمز الذي نسخته من الأداة في **رمز الحساب**، ويبيّن المثال داخل الحقل شكل الرمز.

- اضغط **تفعيل**، فتعرض البطاقة وسم **مفعّل**.

ولتغيير الرمز لاحقًا، اضغط **تعديل** في البطاقة، وحدّث **رمز الحساب**، ثم اضغط **حفظ**.

## Microsoft Clarity

يُثبَّت Clarity عبر Google Tag Manager دون رمز تلصقه، فيتتبّع سلوك زوارك ويمنحك تسجيلات الجلسات والخرائط الحرارية لتحسّن متجرك.

اربط Google Tag Manager بمتجرك قبل البدء. راجع ربط Google Tag Manager .

- ادخل إلى Microsoft Clarity وسجّل الدخول، أو أنشئ حسابًا، ببريدك أو بحساب Google أو Microsoft.

- اضغط **New project**، واملأ بيانات المشروع: اسم متجرك، وعنوانه، وفئة نشاطك، ثم اضغط **Add new project**.

(https://static.zid.store/help-center/shared/apps/13716-01.5e3bd8012c91.webp) أُخفيت البيانات الشخصية.
- يُفتح مشروعك الجديد، فاضغط **View all platforms**.

(https://static.zid.store/help-center/shared/apps/13716-02.77dab2f9ab1c.webp) أُخفيت البيانات الشخصية.
- اختر **Google Tag Manager** من المنصات المدعومة.

(https://static.zid.store/help-center/shared/apps/13716-03.801e1feaa0ba.webp) أُخفيت البيانات الشخصية.
- اضغط **Connect now**.

(https://static.zid.store/help-center/shared/apps/13716-04.3ba10ce47e37.webp) أُخفيت البيانات الشخصية.
- اختر حساب Google الذي تستخدمه في Google Tag Manager.

(https://static.zid.store/help-center/shared/apps/13716-05.7d332667ac02.webp) أُخفيت البيانات الشخصية.
- اضغط **Continue** لتمنح Clarity الصلاحيات التي يطلبها.

(https://static.zid.store/help-center/shared/apps/13716-06.eae12b852882.webp) أُخفيت البيانات الشخصية.
- اختر حسابك في Tag Manager وحاوية متجرك، ثم اضغط **Create and publish**.

(https://static.zid.store/help-center/shared/apps/13716-07.6ba6962b08f2.webp) أُخفيت البيانات الشخصية.
- يؤكد Clarity نجاح الربط، فتظهر بطاقة **Google Tag Manager integration** بوسم **Connected**.

(https://static.zid.store/help-center/shared/apps/13716-08.4be4218c5b47.webp) أُخفيت البيانات الشخصية.
- ولتختبر الربط، زُر متجرك، ثم حدّث صفحة Clarity وافتح **Recordings**.

(https://static.zid.store/help-center/shared/apps/13716-09.ef3a3a13383d.webp) أُخفيت البيانات الشخصية. تظهر زيارتك في التسجيلات بعد قليل، ومعها الصفحة التي دخلت منها وجهازك ودولتك.

(https://static.zid.store/help-center/shared/apps/13716-10.370fe6482564.webp) أُخفيت البيانات الشخصية. وتستطيع ربط Clarity بتطبيق **مايكروسوفت كلاريتي** بدلًا من ذلك: انسخ معرّف المشروع من إعداداته، والصقه في **رمز الحساب** في التطبيق. واكتفِ بطريقة واحدة منهما.

## Hotjar

يتتبّع Hotjar زوار متجرك ويسجّل حركتهم فيه، ويعطيك التفاصيل التي تحتاج إليها لتفهم سلوك العميل وتقيّم أداء متجرك.

- افتح تطبيق **Hotjar** من سوق التطبيقات في زد، فيطلب معرّف الموقع من حسابك في Hotjar.

- وإن لم يكن لديك حساب في Hotjar، فسجّل فيه ببريدك. وتستطيع البدء بالخطة المجانية لتجرّب الخدمة، ثم ترقيتها.

(https://static.zid.store/help-center/shared/apps/4251-03.4ef9f792dd88.webp) أُخفيت البيانات الشخصية.
- يرسل إليك Hotjar رمزًا في بريدك، فأدخله واضغط **Confirm**.

(https://static.zid.store/help-center/shared/apps/4251-04.dcd4a7528e7e.webp) أُخفيت البيانات الشخصية.
- عيّن كلمة مرور تستوفي الشروط الظاهرة، ووافق على شروط الخدمة، ثم اضغط **Next**.

(https://static.zid.store/help-center/shared/apps/4251-05.ac4e297f16c2.webp) أُخفيت البيانات الشخصية.
- اختر كل ما تريد تحقيقه بـ Hotjar، ثم اضغط **Next**.

(https://static.zid.store/help-center/shared/apps/4251-06.e3a314e11a79.webp) أُخفيت البيانات الشخصية.
- أدخل دورك، وهل تدير الحساب لعملاء، واسم مؤسستك وحجمها، ثم اضغط **Next**.

(https://static.zid.store/help-center/shared/apps/4251-07.a17002c99046.webp) أُخفيت البيانات الشخصية.
- أدخل عنوان متجرك ونوع الموقع، ثم اضغط **Start Using Hotjar**.

(https://static.zid.store/help-center/shared/apps/4251-08.3130d7c957de.webp) أُخفيت البيانات الشخصية.
- انسخ **Site ID** الظاهر في صفحة التثبيت، والصقه في **رمز الحساب** بتطبيق **Hotjar** في زد، ثم اضغط **تفعيل**.

(https://static.zid.store/help-center/shared/apps/4251-09.de4a47b868f2.webp) أُخفيت البيانات الشخصية.
- عُد إلى Hotjar، وافتح **Verify installation**، وأدخل عنوان متجرك، ثم اضغط **Verify Installation** ليتأكد أن Hotjar يعمل في متجرك.

(https://static.zid.store/help-center/shared/apps/4251-10.41d6bfb3b047.webp) أُخفيت البيانات الشخصية. ويفتح Hotjar لوحتك بعد التأكيد:

- يجمع **Incoming** في القائمة اليسرى آراء الزوار، فتصفّيها بالفترة والتقييم، وتنشئ أكثر من أداة لجمع الآراء.

(https://static.zid.store/help-center/shared/apps/4251-11.0acb7853d8b1.webp) أُخفيت البيانات الشخصية.
- يعرض **Recordings** رحلة كل زائر: الصفحات التي زارها والوقت الذي قضاه. فصفِّ القائمة، ثم شغّل تسجيلًا لترى تصرّف الزائر في متجرك.

(https://static.zid.store/help-center/shared/apps/4251-12.4acb9bd1ce03.webp) أُخفيت البيانات الشخصية.

## Crazy Egg

يسجّل Crazy Egg كل زيارة من دخول الزائر متجرك حتى خروجه، فتكتشف أنماط التسوق لدى عملائك.

- ادخل إلى Crazy Egg، وأدخل عنوان متجرك، ثم اضغط **Show me my Heatmap**.

(https://static.zid.store/help-center/shared/apps/9326-02.4d43afc1a6ed.webp) أُخفيت البيانات الشخصية.
- سجّل ببريدك الإلكتروني.

(https://static.zid.store/help-center/shared/apps/9326-03.396cc5f82b47.webp) أُخفيت البيانات الشخصية.
- عيّن كلمة مرورك، ووافق على شروط الاستخدام، ثم اضغط **Continue**.

(https://static.zid.store/help-center/shared/apps/9326-04.b47d278e726d.webp) أُخفيت البيانات الشخصية.
- اختر الخطة التي تناسبك، ولكل خطة فترة تجريبية مجانية مدتها 30 يومًا.

(https://static.zid.store/help-center/shared/apps/9326-05.5eef173e7702.webp) أُخفيت البيانات الشخصية.
- أدخل بيانات بطاقتك لإتمام الدفع.

(https://static.zid.store/help-center/shared/apps/9326-06.d1bf912e298c.webp) أُخفيت البيانات الشخصية.
- اضغط **Install Crazy Egg** في لوحة Crazy Egg.

(https://static.zid.store/help-center/shared/apps/9326-07.baae5f7a553a.webp) أُخفيت البيانات الشخصية.
- اختر أن تثبّت رمز التتبع بنفسك.

(https://static.zid.store/help-center/shared/apps/9326-08.04d174ae7c90.webp) أُخفيت البيانات الشخصية.
- يُظهر الرمز رقم حسابك بين `scripts/` و`.js`، وهو مجموعتا أرقام بينهما شرطة مائلة. انسخ هذا الرقم وحده، والصقه في **رمز الحساب** بتطبيق **Crazyegg** في زد، ثم اضغط **تفعيل**.

(https://static.zid.store/help-center/shared/apps/crazy-egg-account-number.ef462497c7fa.webp) انسخ رقم الحساب الواقع بين scripts/ و.js. أُخفيت البيانات الشخصية.
- عُد إلى Crazy Egg واضغط **Next**، وأدخل عنوان متجرك، ثم اضغط **Check URL** ليتأكد من عمل الرمز، واضغط **Next**.

(https://static.zid.store/help-center/shared/apps/9326-10.16ec88c9d16f.webp) أُخفيت البيانات الشخصية. وتفيدك الخرائط الحرارية والتسجيلات حين يزور متجرك عدد كافٍ من الناس، فإن كانت زياراتك قليلة فأمهلها أسابيع قبل أن تبني عليها.

## Contentsquare

يسجّل Contentsquare رحلة الزائر كاملة دون إعداد أحداث أو تتبع يدوي، ويحوّلها إلى رؤى تفاعلية واضحة تُعينك على تحسين تجربة عملائك ومعدلات التحويل.

- أنشئ حسابًا في Contentsquare إن لم يكن لديك.

- افتح **Tag installation** في صفحة **Get started**، وانظر إلى الرمز تحت **Copy the code**.

- انسخ المعرّف الوارد في عنوان السكربت: الحروف والأرقام بعد آخر `/` حتى `.js`.

(https://static.zid.store/help-center/shared/apps/contentsquare-tag.a50e57a952f9.webp) معرّف الوسم هو الجزء الواقع بين /uxa/ و.js في عنوان السكربت. أُخفيت البيانات الشخصية.
- افتح تطبيق **كونتنت سكوير** من سوق التطبيقات في زد، والصق المعرّف في **رمز الحساب**، ثم اضغط **تفعيل**.

- عُد إلى Contentsquare، واضغط **Verify installation**.

## Smartarget

يقدّم Smartarget أدوات تزيد تفاعل زوار متجرك وعملائه.

- افتح تطبيق **Smartarget** من سوق التطبيقات في زد، فيطلب معرّف المستخدم من حسابك في Smartarget.

- وإن لم يكن لديك حساب، فادخل إلى Smartarget واضغط **Sign up for free**.

(https://static.zid.store/help-center/shared/apps/4663-03.7e713f44a0e8.webp) أُخفيت البيانات الشخصية.
- افتح تبويب **Integration**، وانسخ معرّف المستخدم، ثم الصقه في **رمز الحساب** بالتطبيق في زد، واضغط **تفعيل**.

(https://static.zid.store/help-center/shared/apps/smartarget-user-id.acfffe9dd91e.webp) انسخ معرّف المستخدم من تبويب Integration. أُخفيت البيانات الشخصية.
- افتح **Websites** في Smartarget، واضغط **Add website**.

(https://static.zid.store/help-center/shared/apps/4663-05.2a2e27e1a1ca.webp) أُخفيت البيانات الشخصية.
- أدخل عنوان متجرك دون `http` أو `www`، ثم اضغط **Add**.

(https://static.zid.store/help-center/shared/apps/4663-06.98f16dc776a0.webp) أُخفيت البيانات الشخصية.
- تظهر كل المتاجر المضافة إلى حسابك في Smartarget، فاضغط **Configure Apps** تحت المتجر الذي تريده.

(https://static.zid.store/help-center/shared/apps/4663-07.f44074f3d5c9.webp) أُخفيت البيانات الشخصية.
- تصفّح الأدوات حسب تصنيفاتها، واضغط **Connect App** على الأداة التي تريدها، واضبط إعداداتها، ثم احفظها.

(https://static.zid.store/help-center/shared/apps/4663-08.da43cf8ea2b0.webp) أُخفيت البيانات الشخصية. تظهر الأدوات في متجرك بعد حفظ إعداداتها في Smartarget.

تُحمَّل كل أداة تتبع في صفحات متجرك، فإن كنت تستخدم معها Google Tag Manager أو أكثر من بكسل، فتأكد أن صفحاتك ما زالت سريعة التحميل.

## اقرأ أيضًا

- ربط Google Analytics وTag Manager

- ربط بكسل Meta وTikTok وSnapchat وX

- تفاصيل التطبيق وتثبيته

- تطبيقاتي

آخر تحديث: 26 أكتوبر 2026

هل حلّ المقال مشكلتك؟

رأيك يساعدنا نعرف ما يحتاج إلى تحسين.

تحتاج مساعدة إضافية؟

فريق خدمة العملاء جاهز لمساعدتك، أو اعثر على إجابة سريعة في الأسئلة الشائعة.
