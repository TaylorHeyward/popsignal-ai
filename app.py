import logging
import streamlit as st

from src.retriever import get_trend_records
from src.scorer import calculate_trend_score
from src.predictor import predict_trend_label
from src.explainer import generate_explanation


logging.basicConfig(
    filename="popsignal.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


st.set_page_config(
    page_title="PopSignal AI",
    page_icon="🔥",
    layout="wide",
)


def set_custom_styles() -> None:
    st.markdown(
        """
        <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1200px;
        }

        .hero-card {
            background: linear-gradient(135deg, #111827 0%, #1f2937 100%);
            border-radius: 20px;
            padding: 2rem;
            color: white;
            margin-bottom: 1.25rem;
            box-shadow: 0 10px 30px rgba(0,0,0,0.18);
        }

        .hero-title {
            font-size: 2.4rem;
            font-weight: 800;
            margin-bottom: 0.35rem;
            letter-spacing: -0.02em;
        }

        .hero-subtitle {
            font-size: 1.05rem;
            opacity: 0.9;
            line-height: 1.6;
        }

        .section-card {
            background: #f8fafc;
            border: 1px solid #e5e7eb;
            border-radius: 18px;
            padding: 1.2rem 1.25rem;
            margin-bottom: 1rem;
        }

        .result-card-rising {
            background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%);
            border: 1px solid #10b981;
            border-radius: 18px;
            padding: 1rem 1.2rem;
            margin-bottom: 1rem;
        }

        .result-card-peaking {
            background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
            border: 1px solid #f59e0b;
            border-radius: 18px;
            padding: 1rem 1.2rem;
            margin-bottom: 1rem;
        }

        .result-card-fading {
            background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%);
            border: 1px solid #ef4444;
            border-radius: 18px;
            padding: 1rem 1.2rem;
            margin-bottom: 1rem;
        }

        .result-label {
            font-size: 1.25rem;
            font-weight: 800;
            margin-bottom: 0.25rem;
        }

        .result-caption {
            font-size: 0.98rem;
            color: #374151;
            line-height: 1.5;
        }

        .small-muted {
            color: #6b7280;
            font-size: 0.95rem;
        }

        .signal-card {
            background: white;
            border: 1px solid #e5e7eb;
            border-radius: 16px;
            padding: 1rem;
            margin-bottom: 0.75rem;
            box-shadow: 0 4px 14px rgba(0,0,0,0.04);
        }

        .signal-topline {
            font-size: 0.9rem;
            color: #6b7280;
            margin-bottom: 0.6rem;
            font-weight: 600;
        }

        .signal-text {
            font-size: 1rem;
            line-height: 1.65;
            color: #111827;
        }

        .pill {
            display: inline-block;
            padding: 0.28rem 0.6rem;
            border-radius: 999px;
            font-size: 0.8rem;
            font-weight: 700;
            margin-right: 0.4rem;
            margin-bottom: 0.4rem;
            background: #eef2ff;
            color: #3730a3;
        }

        .subsection-title {
            font-size: 1.1rem;
            font-weight: 800;
            margin-bottom: 0.75rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar() -> None:
    with st.sidebar:
        st.title("PopSignal AI")
        st.caption("Cultural momentum analyzer")

        st.markdown("### What it does")
        st.write(
            "PopSignal AI retrieves trend signals from a custom dataset, "
            "scores momentum, and predicts whether a trend is rising, peaking, or fading."
        )

        st.markdown("### Example trends")
        st.write("labubu")
        st.write("doechii")
        st.write("balletcore")
        st.write("mob wife aesthetic")
        st.write("brat aesthetic")

        st.markdown("### What powers the score")
        st.write("• Mentions")
        st.write("• Sentiment")
        st.write("• Recency")

        st.markdown("### Best demo inputs")
        st.write("Use 1 strong trend, 1 mixed trend, and 1 unknown trend.")


def render_hero() -> None:
    st.markdown(
        """
        <div class="hero-card">
            <div class="hero-title">🔥 PopSignal AI</div>
            <div class="hero-subtitle">
                A pop culture trend intelligence app that retrieves signals, scores momentum,
                and predicts whether a trend is rising, peaking, or fading.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_intro() -> None:
    with st.expander("What does this app do?"):
        st.write(
            "PopSignal AI treats culture like a signal system instead of a vague opinion. "
            "It looks up matching trend records, scores them using mentions, sentiment, and recency, "
            "then explains the prediction in plain language."
        )


def render_example_buttons():
    st.markdown("### Quick Try")

    if "trend_name" not in st.session_state:
        st.session_state.trend_name = ""

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        if st.button("labubu", use_container_width=True):
            st.session_state.trend_name = "labubu"
    with c2:
        if st.button("doechii", use_container_width=True):
            st.session_state.trend_name = "doechii"
    with c3:
        if st.button("balletcore", use_container_width=True):
            st.session_state.trend_name = "balletcore"
    with c4:
        if st.button("mob wife aesthetic", use_container_width=True):
            st.session_state.trend_name = "mob wife aesthetic"
    with c5:
        if st.button("brat aesthetic", use_container_width=True):
            st.session_state.trend_name = "brat aesthetic"


def render_result_banner(label: str) -> None:
    if label == "Rising":
        st.markdown(
            """
            <div class="result-card-rising">
                <div class="result-label">Trend is Rising</div>
                <div class="result-caption">
                    Signals indicate increasing cultural momentum and current relevance.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    elif label == "Peaking":
        st.markdown(
            """
            <div class="result-card-peaking">
                <div class="result-label">Trend is Peaking</div>
                <div class="result-caption">
                    Signals show strong visibility, but momentum may be stabilizing rather than accelerating.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class="result-card-fading">
                <div class="result-label">Trend is Fading</div>
                <div class="result-caption">
                    Signals suggest declining intensity, weaker freshness, or reduced enthusiasm.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_metrics(score_data: dict, prediction: dict, signal_count: int) -> None:
    st.markdown("### Trend Snapshot")
    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.metric("Prediction", prediction["label"])
    with m2:
        st.metric("Confidence", prediction["confidence"])
    with m3:
        st.metric("Momentum Score", score_data["final_score"])
    with m4:
        st.metric("Signals Used", signal_count)


def render_signal_breakdown(score_data: dict) -> None:
    st.markdown("### Signal Breakdown")
    st.markdown(
        f"""
        <div class="section-card">
            <div class="pill">Average Mentions: {score_data['average_mentions']}</div>
            <div class="pill">Average Sentiment: {score_data['average_sentiment']}</div>
            <div class="pill">Average Recency: {score_data['average_recency']}</div>
            <div class="small-muted" style="margin-top: 0.8rem;">
                Mentions capture intensity, sentiment captures tone, and recency captures how current the trend is.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_explanation(explanation: str) -> None:
    st.markdown("### Explanation")
    st.markdown(
        f"""
        <div class="section-card">
            {explanation}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_records(records: list[dict]) -> None:
    st.markdown("### Retrieved Trend Signals")

    for index, record in enumerate(records, start=1):
        st.markdown(
            f"""
            <div class="signal-card">
                <div class="signal-topline">
                    Signal {index} • {record['platform']} • {record['date']}
                </div>
                <div style="margin-bottom: 0.65rem;">
                    <span class="pill">Trend: {record['trend']}</span>
                    <span class="pill">Sentiment: {record['sentiment']}</span>
                    <span class="pill">Mentions Score: {record['mentions_score']}</span>
                </div>
                <div class="signal-text">
                    {record['source_text']}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def main() -> None:
    set_custom_styles()
    render_sidebar()
    render_hero()
    render_intro()

    chosen_example = render_example_buttons()

    st.markdown("### Analyze a Trend")
    typed_trend = st.text_input(
    "Enter a trend name",
    key="trend_name",
    placeholder="Try labubu, doechii, balletcore, or brat aesthetic",
)

    analyze_clicked = st.button("Analyze Trend", type="primary", use_container_width=True)

    if analyze_clicked:
        trend_name = typed_trend.strip()

        if not trend_name:
            st.warning("Please enter a valid trend name.")
            logging.warning("User submitted an empty trend name.")
            return

        try:
            records = get_trend_records(trend_name)

            if not records:
                st.error(f"No data found for trend: {trend_name}")
                logging.warning(f"No records found for trend: {trend_name}")
                return

            score_data = calculate_trend_score(records)
            prediction = predict_trend_label(score_data)
            explanation = generate_explanation(
                trend_name=trend_name,
                score_data=score_data,
                prediction=prediction,
                record_count=len(records),
            )

            logging.info(
                f"Trend analyzed: {trend_name} | "
                f"Prediction: {prediction['label']} | "
                f"Score: {score_data['final_score']}"
            )

            st.markdown("---")
            render_result_banner(prediction["label"])
            render_metrics(score_data, prediction, len(records))
            render_signal_breakdown(score_data)
            render_explanation(explanation)
            render_records(records)

        except Exception as error:
            logging.error(f"Error while analyzing trend '{trend_name}': {error}")
            st.error("Something went wrong while analyzing the trend.")


if __name__ == "__main__":
    main()