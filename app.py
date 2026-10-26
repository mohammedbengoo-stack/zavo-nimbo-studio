import streamlit as st 

st.set_page_config(
    page_title="Zavo & Nimbo Studio",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 استوديو زافو ونيمبو")
st.subheader("مغامرات في عالم المقلوب")

st.write("""
مرحباً بك في استوديو إنتاج المسلسل الكرتوني الأصلي
زافو ونيمبو!

هنا نخطط للحلقات والمشاهد والحوار والمؤثرات.
""")

st.header("🎭 الشخصيات الرئيسية")

with st.expander("زافو ZAVO"):
    st.write("""
    مخلوق أزرق صغير، شعره أزرق مع لمسات برتقالية،
    يرتدي نظارات طيار فوق رأسه وسترة مغامرات برتقالية.
    مخترع ومشاكس، يحب التجارب الغريبة.
    """)

with st.expander("نيمبو NIMBO"):
    st.write("""
    مخلوق بنفسجي مستدير، عيناه خضراوان كبيرتان،
    ويرتدي ملابس صفراء وحذاء بنفسجياً.
    طيب وفوضوي، يخاف أحياناً لكنه يلاحظ أشياء لا يلاحظها زافو.
    """)

st.header("🎬 إنشاء مشهد جديد")

episode = st.text_input(
    "اسم الحلقة",
    "الخريطة الغامضة"
)

scene = st.text_area(
    "وصف المشهد",
    "يركض زافو ونيمبو داخل غابة سحرية بينما تتدحرج خلفهما صخرة عملاقة."
)

mood = st.selectbox(
    "نوع المشهد",
    ["كوميدي", "مغامرة", "غموض", "مفاجأة"]
)

if st.button("إنشاء وصف المشهد"):
    st.success("تم إعداد وصف المشهد!")
    st.write("الحلقة:", episode)
    st.write("النوع:", mood)
    st.text_area(
        "انسخ هذا الوصف إلى مولّد الفيديو",
        f"""Original 3D animated cartoon.
Zavo: small blue fantasy creature with orange adventure clothes and pilot goggles.
Nimbo: round purple creature with large green eyes and yellow clothes.
Scene: {scene}
Mood: {mood}
Keep character designs consistent.
Colorful magical world, expressive cartoon comedy.
No text, no subtitles, no logos.""",
        height=220
    )

st.info(
    "هذا التطبيق ينظم أوصاف المشاهد. "
    "توليد الفيديو الفعلي يحتاج إلى خدمة فيديو منفصلة."
)