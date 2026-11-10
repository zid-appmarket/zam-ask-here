---
# Synced from https://help.zid.sa/ar/apps/google-tools
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: mh-apps-google-tools
title: "ربط Google Analytics وTag Manager بمتجرك في زد"
product: zam
audience: all
status: verified
updated: 2026-10-26
source_url: https://help.zid.sa/ar/apps/google-tools
tags: [from-docs-site, merchant-help-center]
language: ar
---

> أضف إلى متجرك معرّف القياس في Google Analytics ومعرّف حاوية Tag Manager، وأضف أكواد التتبع والأدوات عبر Tag Manager.
# ربط Google Analytics وTag Manager بمتجرك في زد

يُعرّفك Google Analytics بزوار متجرك وكيف وصلوا إليه، ويتيح لك Google Tag Manager إضافة رموز التتبع والأدوات إلى متجرك دون المساس بثيمك. ولكلٍّ منهما تطبيق مجاني في سوق التطبيقات ، فابحث عنه باسمه أو افتح تصنيف **تتبع الحملات والإسناد**.

الأداة ما تقدمه لمتجرك ما تضيفه في زد

**Google Analytics** تقارير عن الزوار ومصادر الزيارات والأجهزة والسلوك والمبيعات معرّف القياس، ويبدأ بـ `G-`

**Google Tag Manager** إضافة الوسوم، كرموز التتبع والأزرار، وإدارتها من حساب Google واحد معرّف الحاوية، ويبدأ بـ `GTM-`

استخدم حساب Google خاصًّا بنشاطك، واجعله واحدًا لأدوات Google كلها، ليرتبط بعضها ببعض. ويعتمد عليه دليلان آخران: عرض منتجاتك على Google عبر Merchant Center و إثبات ملكية متجرك في Google Search Console .

## ربط Google Analytics

يقدّم Google Analytics مجانًا تحليلات دقيقة لمتجرك:

- الأداء والمبيعات: عدد الزوار، والمبيعات، والمنتجات الأكثر رواجًا.

- سلوك العملاء: تفاعلهم مع متجرك.

- أثر التسويق: نتائج حملاتك التسويقية.

- معدلات التحويل: أين يتوقف المتسوقون قبل إتمام الشراء.

- تقارير مخصصة على قدر حاجتك.

- جمهورك: مواقع الزوار الجغرافية وبياناتهم الديموغرافية.

- مواضع التحسين في متجرك.

- سجّل الدخول إلى Google Analytics، وأنشئ حسابًا يُفضَّل أن يحمل اسم متجرك. وأدخل في **تفاصيل الحساب** اسمه، واختر إعدادات مشاركة البيانات.

(https://static.zid.store/help-center/shared/apps/9443-01.abbadecf0308.webp) أُخفيت البيانات الشخصية.
- أدخل في خطوة **إنشاء موقع** اسم متجرك اسمًا للموقع، ثم اختر منطقته الزمنية ودولته وعملته.

(https://static.zid.store/help-center/shared/apps/9443-02.6c2a2a12efe4.webp) أُخفيت البيانات الشخصية.
- حدّد في **تفاصيل الأعمال** فئة نشاطك وحجمه.

(https://static.zid.store/help-center/shared/apps/9443-03.7499b49d2b49.webp) أُخفيت البيانات الشخصية.
- اختر أهدافك من استخدام Google Analytics لنشاطك، ثم اضغط **إنشاء**.

(https://static.zid.store/help-center/shared/apps/9443-04.ea76d90a38b6.webp) أُخفيت البيانات الشخصية.
- اختر دولتك في نافذة شروط Google Analytics وأحكامه، ثم اضغط **أوافق**.

(https://static.zid.store/help-center/shared/apps/9443-05.dd99f2330ff5.webp) أُخفيت البيانات الشخصية.
- اختر **الويب** مصدرًا لجمع البيانات.

(https://static.zid.store/help-center/shared/apps/9443-06.ae5463a3afce.webp) أُخفيت البيانات الشخصية.
- أدخل عنوان متجرك واسمًا لمصدر البيانات، ثم أنشئه. واكتب العنوان دون `https://`، فالحقل يبدأ به.

(https://static.zid.store/help-center/shared/apps/9443-07.2bf60199af5f.webp) أُخفيت البيانات الشخصية.
- انسخ معرّف القياس الظاهر في تفاصيل مصدر البيانات، ويبدأ بـ `G-`.

(https://static.zid.store/help-center/shared/apps/9443-08.89a20c9fa212.webp) أُخفيت البيانات الشخصية.
- افتح **التطبيقات** > **سوق التطبيقات** في لوحة تحكم زد، وابحث عن **Google Analytics**، ثم افتح التطبيق واضغط **تفعيل**.

- الصق المعرّف في **رمز الحساب** ببطاقة **تفعيل التطبيق**، ثم اضغط **تفعيل**.

يبدأ Analytics جمع البيانات من زائرك التالي، فافتح تقرير الوقت الفعلي فيه وزُر متجرك من جهاز آخر لترى الزيارة.

## ربط Google Tag Manager

يحفظ Tag Manager رموز التتبع في حاوية، فإذا أضفتها إلى متجرك أضفت الرموز وعدّلتها وحذفتها من Tag Manager دون أي تغيير في زد.

- سجّل الدخول إلى Google Tag Manager، واضغط **Create Account**.

(https://static.zid.store/help-center/shared/apps/3802-01.80a967354873.webp) أُخفيت البيانات الشخصية.
- أدخل في **Account Setup** اسم الحساب ودولته، وفي **Container Setup** اسمًا للحاوية كعنوان متجرك، واختر **Web** منصةً مستهدفة.

(https://static.zid.store/help-center/shared/apps/3802-02.ef1df8b93eb5.webp) أُخفيت البيانات الشخصية.
- اضغط **Create**.

(https://static.zid.store/help-center/shared/apps/3802-03.79a616f204c3.webp) أُخفيت البيانات الشخصية.
- اقرأ شروط خدمة Google Tag Manager، وحدّد مربع الموافقة على شروط معالجة البيانات، ثم اضغط **Yes**.

(https://static.zid.store/help-center/shared/apps/3802-04.cdf5fb83fa94.webp) أُخفيت البيانات الشخصية.
- تُفتح حاويتك، فانسخ معرّفها الظاهر أعلى مساحة العمل، ويبدأ بـ `GTM-`.

(https://static.zid.store/help-center/shared/apps/gtm-container-id.528f10ff2937.webp) يظهر معرّف الحاوية أعلى مساحة العمل. أُخفيت البيانات الشخصية.
- افتح تطبيق **Google Tag Manager** من سوق التطبيقات في زد، واضغط **تفعيل**.

- الصق المعرّف في **رمز الحساب**، ثم اضغط **تفعيل**.

يُحمَّل كل ما تنشره في Tag Manager في واجهة متجرك ويظهر لعملائك فورًا، فزر واتساب أو نافذة المحادثة المباشرة التي تضيفها عبره تظهر في صفحات متجرك دون أي تعديل آخر. ويحتاج Tag Manager إلى معرفة تقنية، فاستخدمه بحذر: يُحمَّل كل رمز مع فتح كل صفحة، وتُبطئ الرموز الكثيرة أو الثقيلة أو غير الضرورية متجرك. فاحذف الوسوم التي لم تعد تحتاجها، واستخدم لـ Snapchat وTikTok تطبيقيهما في زد بدل Tag Manager، فتتبعهما أدق. راجع ربط بكسل Meta وTikTok وSnapchat وX .

## الوسوم والمشغّلات والمتغيرات

العنصر ما هو

**الوسم** (Tag) رمز يرسل معلومات إلى نظام آخر، كتتبع سلوك الزوار أو إضافة زر إلى واجهة متجرك.

**المشغّل** (Trigger) قاعدة تحدد متى يعمل الوسم، إذ يراقب أحداثًا كالنقرات، فإذا طابق حدثٌ شروطَه شغّل كل الوسوم المرتبطة به تلقائيًا.

**المتغير** (Variable) قيمة مسمّاة تُملأ تلقائيًا عند تشغيل الرمز، كعنوان الصفحة، وتعتمد عليها الوسوم والمشغّلات في عملها.

## إضافة وسم إلى متجرك

يضيف هذا المثال زر واتساب بلصق الرمز الذي تعطيك إياه أداة المحادثة، وتُضاف أي أداة أخرى بالطريقة نفسها.

- اضغط **Add a new tag** في مساحة العمل.

(https://static.zid.store/help-center/shared/apps/3802-08.c844b3a5b61f.webp) أُخفيت البيانات الشخصية.
- اضغط القلم في **Tag Configuration**.

(https://static.zid.store/help-center/shared/apps/3802-09.6deeaaea8f03.webp) أُخفيت البيانات الشخصية.
- اختر نوع الوسم، فإن وجدت الأداة التي تضيفها في القائمة فاخترها، وإلا فاختر **Custom HTML**.

(https://static.zid.store/help-center/shared/apps/3802-10.064284a20dc6.webp) أُخفيت البيانات الشخصية.
- الصق رمز الأداة في مربع **HTML**.

(https://static.zid.store/help-center/shared/apps/3802-11.e1ed1a76de1e.webp) أُخفيت البيانات الشخصية.
- ولتظهر الأداة في كل صفحات متجرك، اضغط القلم في **Triggering**.

(https://static.zid.store/help-center/shared/apps/3802-12.112b9d898b11.webp) أُخفيت البيانات الشخصية.
- حدّد **All Pages**، ثم اضغط **Add**.

(https://static.zid.store/help-center/shared/apps/3802-13.f81b1dfbab44.webp) أُخفيت البيانات الشخصية.
- اضغط **Save**.

(https://static.zid.store/help-center/shared/apps/3802-14.894bdb7b4506.webp) أُخفيت البيانات الشخصية.
- سمِّ الوسم باسم الأداة، ثم اضغط **Save**.

(https://static.zid.store/help-center/shared/apps/3802-15.85b93d35d68a.webp) أُخفيت البيانات الشخصية.
- اضغط **Submit**.

(https://static.zid.store/help-center/shared/apps/3802-16.5eaaffad3758.webp) أُخفيت البيانات الشخصية.
- أضف اسمًا ووصفًا لهذه النسخة إن شئت، ثم اضغط **Continue**، أو **Skip**.

(https://static.zid.store/help-center/shared/apps/3802-17.4444b8bf09f8.webp) أُخفيت البيانات الشخصية.
- اضغط **Publish**.

(https://static.zid.store/help-center/shared/apps/3802-18.cfeb84512423.webp) أُخفيت البيانات الشخصية. تظهر الأداة في متجرك بعد 10 إلى 15 دقيقة من النشر.

## التنقل في Tag Manager

يضم Tag Manager ثلاثة تبويبات: **Workspace** و**Versions** و**Admin**.

(https://static.zid.store/help-center/shared/apps/8943-01.bf9a350975eb.webp) أُخفيت البيانات الشخصية. ففي **Workspace** تبني حاويتك:

القسم ما يضمه

**Overview** لمحة عن آخر التعديلات على وسومك.

**Tags** وسومك، لتضيفها وتعدّلها وتحذفها.

**Triggers** مشغّلاتك، لتضيفها وتعدّلها وتحذفها.

**Variables** **Built-In Variables** الجاهزة من Google والشائعة في الوسوم، و**User-Defined Variables** التي تنشئها.

**Folders** مجلدات ترتّب وسومك ومشغّلاتك ومتغيراتك في مجموعات يسهل الوصول إليها.

**Templates** تعريفاتك الخاصة للوسوم والمتغيرات، يستعملها فريقك إلى جانب قوالب Tag Manager الجاهزة.

(https://static.zid.store/help-center/shared/apps/8943-02.f637fd517da2.webp) أُخفيت البيانات الشخصية. ويسرد **Versions** النسخ التي نشرتها، مع عدد وسوم كلٍّ منها ومشغّلاتها ومتغيراتها ووقت نشرها.

(https://static.zid.store/help-center/shared/apps/8943-03.3319b85fc658.webp) أُخفيت البيانات الشخصية. ويُدير **Admin** الحساب والحاوية: إعداداتهما، وآخر ما جرى فيهما، ومن يستطيع استخدامهما.

(https://static.zid.store/help-center/shared/apps/8943-04.e836b772fffb.webp) أُخفيت البيانات الشخصية.

## منح فريقك صلاحية Tag Manager

- اضغط **User Management** في تبويب **Admin**، فتظهر قائمة بكل من يصل إلى Tag Manager.

- اضغط **+** لإضافة مستخدم.

(https://static.zid.store/help-center/shared/apps/8943-06.b3b9edc30974.webp) أُخفيت البيانات الشخصية.
- أدخل البريد الإلكتروني للمستخدم الجديد.

(https://static.zid.store/help-center/shared/apps/8943-07.db230edc1a03.webp) أُخفيت البيانات الشخصية.
- اختر صلاحياته، ثم اضغط **Invite**.

(https://static.zid.store/help-center/shared/apps/8943-08.a9e714b88f4b.webp) أُخفيت البيانات الشخصية. وتتدرج صلاحيات الحاوية الأربع، فتضم كلٌّ منها ما قبلها:

الصلاحية ما يستطيعه صاحبها

**Read** الاطلاع على الوسوم والمشغّلات والمتغيرات دون تعديلها.

**Edit** إنشاء مساحات العمل وتعديل الوسوم والمشغّلات والمتغيرات.

**Approve** إنشاء نسخ الحاوية جاهزةً للنشر.

**Publish** نشر النسخ في متجرك، وتشمل الصلاحيات السابقة كلها.

ويقبل المدعوّ الدعوة من البريد الذي يرسله إليه Google.

## إن لم تظهر البيانات

المشكلة ما تتحقق منه

لا تظهر زيارات في Analytics يبدأ المعرّف في زد بـ `G-` ويخص مصدر بيانات عنوان متجرك، واضغط **تعديل** لتصحيحه.

لا يعمل وسم في Tag Manager نُشرت آخر نسخة من الحاوية، وللوسم مشغّل.

أبطأ متجرك احذف الوسوم التي لم تعد تحتاجها، وافحص الرموز الثقيلة كأدوات المحادثة واحدًا واحدًا.

## اقرأ أيضًا

- عرض منتجاتك على Google عبر Merchant Center

- إثبات ملكية متجرك في Google Search Console

- تحسين الظهور وكاتالوج المنتجات

- ربط بكسل Meta وTikTok وSnapchat وX

- ربط Clarity وHotjar وCrazy Egg وContentsquare وSmartarget

- تفاصيل التطبيق وتثبيته

آخر تحديث: 26 أكتوبر 2026

هل حلّ المقال مشكلتك؟

رأيك يساعدنا نعرف ما يحتاج إلى تحسين.

تحتاج مساعدة إضافية؟

فريق خدمة العملاء جاهز لمساعدتك، أو اعثر على إجابة سريعة في الأسئلة الشائعة.
