CUSTOM_CSS = """
<style>

/* Main Background */
.stApp {
    background: linear-gradient(
        135deg,
        #030712,
        #0f172a,
        #111827
    );
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(8,15,30,0.95);
    border-right: 1px solid rgba(255,255,255,0.08);
}

/* Headers */
h1,h2,h3 {
    color: white !important;
}

/* Metric Cards */
[data-testid="stMetric"] {

    background: rgba(255,255,255,0.04);

    backdrop-filter: blur(15px);

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 24px;

    box-shadow:
        0 0 20px rgba(59,130,246,0.15);

    transition: all .3s ease;
}

[data-testid="stMetric"]:hover {

    transform:
        translateY(-8px)
        scale(1.03);

    box-shadow:
        0 0 35px rgba(59,130,246,0.35);
}
/* Buttons */
.stButton button {
    width: 100%;
    border-radius: 15px;
    background: linear-gradient(
        90deg,
        #2563eb,
        #7c3aed
    );
    color: white;
    border: none;
}


/* Expander */
.streamlit-expanderHeader {
    border-radius: 15px;
}

/* Glow Effect */
.glow {
    text-align:center;
    font-size:60px;
    font-weight:bold;
    color:white;

    text-shadow:
    0 0 15px #3b82f6,
    0 0 35px #3b82f6,
    0 0 70px #2563eb;
}

.main .block-container {
    background: rgba(10,20,50,0.45);
    backdrop-filter: blur(20px);
    border-radius: 30px;
    padding: 2rem;
    border: 1px solid rgba(255,255,255,0.08);

    box-shadow:
    0 0 50px rgba(59,130,246,0.15);
}

.stApp {
    background:
    radial-gradient(circle at 20% 20%, rgba(59,130,246,0.15), transparent 30%),
    radial-gradient(circle at 80% 30%, rgba(168,85,247,0.15), transparent 30%),
    radial-gradient(circle at 50% 80%, rgba(37,99,235,0.15), transparent 30%),
    #020617;

    animation: bgMove 15s ease infinite;
}

@keyframes bgMove {

    0% {
        background-position: 0% 0%;
    }

    50% {
        background-position: 100% 50%;
    }

    100% {
        background-position: 0% 0%;
    }
}

.block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
}

textarea {
    background: rgba(255,255,255,0.05) !important;
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 30px !important;
    width:100% !important;
}

.stButton button:hover {
    box-shadow:
    0 0 15px #3b82f6,
    0 0 30px #7c3aed;

    transform: translateX(5px);
}

.hero-card{
    width:100%;
    max-width:900px;
    margin:25px auto;

    padding:25px;

    border-radius:24px;

    text-align:center;

    background:rgba(255,255,255,0.05);

    backdrop-filter:blur(15px);

    border:1px solid rgba(255,255,255,0.15);

    box-shadow:
        0 0 20px rgba(0,120,255,0.25),
        0 0 60px rgba(120,0,255,0.15);

    color:white;

    transition:0.3s ease;
}

.block-container{
    padding-bottom: 1rem !important;
}

.main{
    margin-bottom:0 !important;
}

section.main{
    padding-bottom:0 !important;
}

/* Fix Streamlit vertical spacing */
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 0rem !important;
    max-width: 1400px;
}

/* Remove excessive gaps */
.element-container {
    margin-bottom: 0.5rem !important;
}

/* Reduce markdown spacing */
.stMarkdown {
    margin-bottom: 0rem !important;
}

/* Hero card spacing */
.hero-card {
    margin-top: 15px !important;
    margin-bottom: 20px !important;
}

/* Remove empty container spacing */
div[data-testid="stVerticalBlock"] > div:empty {
    display: none;
}



.stButton button{
    width:220px;
    height:55px;
    border-radius:18px;
    font-size:18px;
    font-weight:600;
}

.status-card{

    margin-top:20px;

    padding:22px;

    border-radius:22px;

    background:rgba(255,255,255,0.05);

    backdrop-filter:blur(15px);

    border:1px solid rgba(255,255,255,0.12);

    color:white;

    line-height:1.8;

    box-shadow:
        0 0 20px rgba(59,130,246,0.15);
}

[data-testid="stMetricValue"]{

    text-align:center !important;

    width:100%;
}

[data-testid="stMetricLabel"]{

    text-align:center !important;

    width:100%;
}

</style>
"""