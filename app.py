import streamlit as st
import json
import random
import io
import zipfile

st.set_page_config(
    page_title="Zavo & Nimbo Studio",
    page_icon="🎬",
    layout="wide"
)

# =========================
# إعداد الاستوديو
# =========================

st.title("🎬 استوديو زافو ونيمبو")
st.subheader("مغامرات في عالم المقلوب")
st.caption("استوديو مستقل لتخطيط الحلقات والمشاهد وتجهيز أوصاف الفيديو")

st.info(
    "هذا الاستوديو يساعدك على كتابة القصص وتجهيز المشاهد. "
    "توليد الفيديو الفعلي يتم باستخدام أداة فيديو خارجية."
)

# =========================
# دليل الشخصيات
# =========================

CHARACTERS = """
ZAVO:
A small blue fantasy creature, orange tufts of hair,
pilot goggles on his head, orange adventure jacket,
dark trousers, oversized shoes.
Inventive, mischievous, curious, and overconfident.

NIMBO:
A round purple fantasy creature, large green eyes,
green belly, yellow overalls, purple shoes.
Kind, clumsy, funny, and easily frightened.

Keep both characters visually consistent in every scene.
Do not change their colors, clothes, body shapes, or eyes.
"""

st.header("🎭 دليل الشخصيات")

with st.expander("زافو ZAVO"):
    st.write(
        "مخلوق أزرق صغير، خصلات برتقالية، "
        "نظارات طيار فوق الرأس، وسترة مغامرات برتقالية. "
        "مخترع ومشاكس وواثق بنفسه أكثر من اللازم."
    )

with st.expander("نيمبو NIMBO"):
    st.write(
        "مخلوق بنفسجي مستدير، عينان خضراوان كبيرتان، "
        "بطن أخضر، أفرول أصفر وحذاء بنفسجي. "
        "طيب وفوضوي ويخاف بسهولة."
    )

# =========================
# إنشاء فكرة الحلقة
# =========================

st.header("📚 مخطط الحلقة")

episode_number = st.number_input(
    "رقم الحلقة",
    min_value=1,
    max_value=999,
    value=1,
    step=1
)

episode_title = st.text_input(
    "عنوان الحلقة",
    value="الخريطة التي تضحك"
)

duration = st.selectbox(
    "المدة المستهدفة",
    ["30 ثانية", "60 ثانية", "90 ثانية", "دقيقتان", "3 دقائق"]
)

style = st.selectbox(
    "نوع المغامرة",
    [
        "مغامرة كوميدية غامضة",
        "مطاردة مضحكة",
        "اختراع ينقلب على صاحبه",
        "لغز في عالم المقلوب",
        "مغامرة في مكان مستحيل",
        "كنز له سر غير متوقع"
    ]
)

custom_idea = st.text_area(
    "فكرتك الخاصة (اختياري)",
    placeholder="مثال: يجد زافو بابًا لا يفتح إلا عندما يضحك نيمبو..."
)

# =========================
# مكتبة بذور القصص
# =========================

story_seeds = [
    {
        "place": "مكتبة تطير كتبها كلما كذب أحد",
        "problem": "كتاب صغير يسرق ظلال الشخصيات",
        "twist": "الظل المسروق يبدأ بالتصرف كأنه البطل الحقيقي"
    },
    {
        "place": "سوق تُباع فيه الأصوات داخل فقاعات",
        "problem": "يبتلع نيمبو صوت زافو بالخطأ",
        "twist": "الصوت يبدأ بإعطاء أوامر غريبة من داخل بطن نيمبو"
    },
    {
        "place": "جزيرة تتحرك عندما ينظر إليها أحد",
        "problem": "يحاول الصديقان الوصول إلى صندوق متحرك",
        "twist": "يكتشفان أن الجزيرة نفسها تحاول الهرب منهما"
    },
    {
        "place": "مصنع يصنع نسخًا من الأشياء التي لا يفكر فيها أحد",
        "problem": "يظهر زر غامض يضاعف كل شيء يلمسه",
        "twist": "تتضاعف المشكلة نفسها في كل مرة يحاولان حلها"
    },
    {
        "place": "غابة تنمو أشجارها إلى الأسفل نحو السماء",
        "problem": "تختفي الطريق كلما اقتربا من نهايتها",
        "twist": "الطريق ليست طريقًا، بل مخلوق نائم"
    },
    {
        "place": "محطة قطار تصل فيها القطارات قبل أن تغادر",
        "problem": "يركبان قطارًا يحمل رسالة من المستقبل",
        "twist": "الرسالة كتبها أحدهما، لكن بخط لا يعرفه"
    },
    {
        "place": "متحف تحفظ فيه المتاهات بدل اللوحات",
        "problem": "تخرج متاهة صغيرة من إطارها وتلاحقهما",
        "twist": "المتاهة تخاف من الفئران الورقية التي تصنعها بنفسها"
    },
    {
        "place": "بحيرة تسقط قطرات الماء منها إلى الأعلى",
        "problem": "يعلق نيمبو داخل فقاعة لا تتوقف عن الصعود",
        "twist": "الفقاعة تصل إلى سمكة ترتدي حذاءً وتبحث عن البحر"
    }
]

# =========================
# مشاهد الحلقة
# =========================

st.header("🎥 توليد خطة المشاهد")

scene_count = st.slider(
    "عدد المشاهد",
    min_value=3,
    max_value=10,
    value=5
)

if "production" not in st.session_state:
    st.session_state.production = {}

if st.button("✨ أنشئ خطة مغامرة جديدة", type="primary"):

    seed = random.choice(story_seeds)

    if custom_idea.strip():
        central_problem = custom_idea.strip()
    else:
        central_problem = seed["problem"]

    scenes = [
        {
            "name": "الافتتاحية الخاطفة",
            "action": (
                f"يفتتح المشهد في {seed['place']}. "
                "يظهر زافو وهو يضغط زرًا غريبًا، "
                "بينما يحاول نيمبو منعه في اللحظة الأخيرة."
            ),
            "emotion": "مفاجأة وضحك",
            "camera": "لقطة واسعة ثم تقريب سريع على وجهي الشخصيتين",
            "sound": "صوت طقطقة غامض ثم مؤثر كوميدي مفاجئ"
        },
        {
            "name": "ظهور المشكلة",
            "action": (
                f"تبدأ المشكلة: {central_problem}. "
                "يحاول زافو التصرف وكأنه يعرف ما يحدث، "
                "بينما يكتشف نيمبو أن الوضع أسوأ مما يبدو."
            ),
            "emotion": "فضول وارتباك",
            "camera": "لقطات متوسطة مع حركة كاميرا مرحة",
            "sound": "أصوات غريبة متتابعة وموسيقى مغامرات خفيفة"
        },
        {
            "name": "الخطة الكارثية",
            "action": (
                "يصنع زافو خطة مرتجلة باستخدام أشياء مستحيلة. "
                "يوافق نيمبو على مساعدته، لكنه يمسك الشيء الخطأ "
                "ويشغّل سلسلة أحداث غير متوقعة."
            ),
            "emotion": "حماس وفوضى",
            "camera": "حركة جانبية سريعة ولقطات قريبة للتعبيرات",
            "sound": "أصوات ميكانيكية وقفزات كوميدية"
        },
        {
            "name": "الانقلاب غير المتوقع",
            "action": (
                f"تحدث مفاجأة تقلب الموقف: {seed['twist']}. "
                "يظن الصديقان أنهما فازا، ثم يكتشفان "
                "أن المشكلة أصبحت أكبر بطريقة مضحكة."
            ),
            "emotion": "دهشة وضحك",
            "camera": "لقطة واسعة للمفاجأة ثم تقريب على رد الفعل",
            "sound": "صمت قصير ثم مؤثر كوميدي قوي"
        },
        {
            "name": "نهاية تفتح مغامرة جديدة",
            "action": (
                "ينجح الصديقان في الهرب بصعوبة، "
                "لكن يظهر جسم صغير غامض يحمل علامة لا يعرفانها. "
                "ينظر زافو إلى نيمبو ويقول: "
                "يبدو أن هذه كانت البداية فقط!"
            ),
            "emotion": "فرح وغموض",
            "camera": "لقطة خلفية ثم تقريب على الجسم الغامض",
            "sound": "موسيقى انتصار قصيرة يعقبها صوت غامض"
        }
    ]

    chosen = scenes[:scene_count]

    st.session_state.production = {
        "episode": int(episode_number),
        "title": episode_title,
        "duration": duration,
        "style": style,
        "idea": central_problem,
        "scenes": chosen,
        "statuses": ["جاهز للتوليد"] * len(chosen)
    }

# =========================
# عرض النتائج
# =========================

data = st.session_state.production

if data:
    st.success("تم إعداد خطة الحلقة!")

    st.subheader(
        f"الحلقة {data['episode']}: {data['title']}"
    )

    st.write("المدة:", data["duration"])
    st.write("النوع:", data["style"])
    st.write("الفكرة المحورية:", data["idea"])

    st.divider()

    for i, scene in enumerate(data["scenes"]):
        with st.expander(
            f"المشهد {i + 1}: {scene['name']}",
            expanded=(i == 0)
        ):
            st.write("**الأحداث:**", scene["action"])
            st.write("**المشاعر:**", scene["emotion"])
            st.write("**الكاميرا:**", scene["camera"])
            st.write("**الصوت:**", scene["sound"])

            prompt = f"""
Create an original, colorful 3D animated family adventure.
Scene: {scene['action']}

CHARACTER DESIGN LOCK:
{CHARACTERS}

VISUAL DIRECTION:
{scene['emotion']}.
Camera: {scene['camera']}.
Sound idea: {scene['sound']}.

Smooth animation, expressive faces, readable physical comedy,
cinematic lighting, clear staging, family-friendly humor.
Preserve character proportions, colors, clothing, and appearance.
No text, no subtitles, no logos.
"""

            st.text_area(
                "وصف الفيديو الجاهز للنسخ",
                value=prompt.strip(),
                height=300,
                key=f"prompt_{i}"
            )

            data["statuses"][i] = st.selectbox(
                "حالة المشهد",
                [
                    "قيد التخطيط",
                    "جاهز للتوليد",
                    "تم توليد الفيديو",
                    "يحتاج إلى إعادة العمل"
                ],
                index=[
                    "قيد التخطيط",
                    "جاهز للتوليد",
                    "تم توليد الفيديو",
                    "يحتاج إلى إعادة العمل"
                ].index(data["statuses"][i]),
                key=f"status_{i}"
            )

    # =========================
    # تنزيل ملفات المشروع
    # =========================

    project_json = json.dumps(
        data,
        ensure_ascii=False,
        indent=2
    )

    st.download_button(
        "⬇️ تنزيل بيانات الحلقة JSON",
        data=project_json.encode("utf-8"),
        file_name=f"zavo_nimbo_episode_{data['episode']}.json",
        mime="application/json"
    )

    text_file = io.StringIO()

    text_file.write(
        f"زافو ونيمبو - الحلقة {data['episode']}\n"
    )
    text_file.write(f"العنوان: {data['title']}\n\n")

    for i, scene in enumerate(data["scenes"]):
        text_file.write(
            f"\nالمشهد {i + 1}: {scene['name']}\n"
        )
        text_file.write(f"الأحداث: {scene['action']}\n")
        text_file.write(f"المشاعر: {scene['emotion']}\n")
        text_file.write(f"الكاميرا: {scene['camera']}\n")
        text_file.write(f"الصوت: {scene['sound']}\n")
        text_file.write(
            f"الحالة: {data['statuses'][i]}\n"
        )

    st.download_button(
        "📄 تنزيل خطة الحلقة TXT",
        data=text_file.getvalue().encode("utf-8"),
        file_name=f"zavo_nimbo_episode_{data['episode']}.txt",
        mime="text/plain"
    )

    st.caption(
        "ملاحظة: الأفكار والأوصاف مولدة من قوالب وقواعد داخلية، "
        "وليست نموذج ذكاء اصطناعي خارجيًا. راجع النصوص قبل النشر."
    )

else:
    st.warning(
        "اختر عنوان الحلقة ونوع المغامرة، "
        "ثم اضغط «أنشئ خطة مغامرة جديدة»."
    )

st.divider()
st.caption(
    "ZAVO & NIMBO STUDIO — Original story planning and scene production."
)