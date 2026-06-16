import os
import re
from youtube_transcript_api import YouTubeTranscriptApi

TRANSCRIPTS = {
    "aleyda-solis": [
        ("m3M_tal884c", "The State and Future of Search QA with Danny Sullivan"),
        ("-4cu882OJ8E", "Traditional SEO vs AI Search Optimization GEO AEO"),
        ("LGvbEHyX5oE", "Google AI Mode vs Traditional Search"),
    ],
    "lily-ray": [
        ("mgI1U7XPsUA", "How SEO is Evolving in 2025"),
        ("2nJkT8zOzcM", "GEO AEO LLMO Separating Fact from Fiction MozCon 2025"),
        ("2vtFN9lDciM", "AI Search 2025 Recap and 2026 Game Plan"),
    ],
    "mike-king": [
        ("pQLivtcqCZs", "Relevance Engineering AI Search and Query Fan Out"),
        ("WEoVn1i76D8", "Mike King discusses the RAG Pipeline"),
        ("hDYQ3AqMOOs", "Query Fan Out What it is and What You Should Do"),
    ],
    "eli-schwartz": [
        ("Z71yGshPTwk", "Rethinking SEO in the age of AI Lennys Podcast"),
    ],
    "kevin-indig": [
        ("jQXvbeYF5go", "Google Will Kill Your Traffic Heres How You Adapt"),
        ("qujABKOAThA", "SEO in the Age of AI Google Overviews Future of Search"),
        ("FE5iOW0mpX4", "3 SEO Necessities for the AI Era"),
    ],
    "ross-hudgens": [
        ("8-PS7gR2G0I", "AI Visibility Data Journalism and the Future of SEO"),
    ],
    "bernard-huang": [
        ("RMg2eTZL7Jk", "How To Do AEO Live Session with Bernard Huang"),
        ("TpXnYqLeu2g", "Future of Search and AI by Bernard Huang"),
        ("f84ovVChEh4", "AI-driven SEO revolution future of discoverability"),
    ],
    "tim-soulo": [
        ("1J26dKqzzgg", "Where Marketings Headed Ahrefs Evolve 2025"),
        ("D7LBx8RFOcQ", "AI Writing at Scale Ahrefs Step-by-Step Workflow"),
        ("EbT3LE-Y2gk", "Tim Soulo vs Glen Allsopp Ahrefs Use Case Showdown"),
    ],
    "andy-crestodina": [
        ("8cey3LA_1K0", "The AI Impact on SEO with Andy Crestodina"),
        ("nMxIprRHjuU", "Andy Crestodina on SEO Content Gaps and Using AI"),
        ("1hcv93CwulE", "SEO Isnt Dead Youre Just Doing It Wrong"),
    ],
    "glen-allsopp": [
        ("XSLoLghiW74", "AI Apps Reports and Workflows Every Marketer Should Steal"),
    ],
}


def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text.strip('-')


def fetch_one(video_id):
    try:
        api = YouTubeTranscriptApi()
        fetched = api.fetch(video_id, languages=['en', 'en-US', 'en-GB'])
        try:
            return "\n".join(s.text for s in fetched)
        except AttributeError:
            return "\n".join(s["text"] for s in fetched.to_raw_data())
    except Exception as e:
    return f"[Could not fetch transcript for {video_id}: {e}]"


def main():
    base = os.path.join("research", "youtube-transcripts")
    ok, failed = 0, 0
    for author, videos in TRANSCRIPTS.items():
        author_dir = os.path.join(base, author)
        os.makedirs(author_dir, exist_ok=True)
        for video_id, title in videos:
            print(f"Fetching {video_id} for {author}...")
            text = fetch_one(video_id)
            if text.startswith("[Could not"):
                failed += 1
                print(f"  FAILED: {text}")
            else:
                ok += 1
            filepath = os.path.join(author_dir, f"{slugify(title)}.md")
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"# {title}\n\n")
                f.write(f"Author: {author}\n")
                f.write(f"Video ID: {video_id}\n")
                f.write(f"URL: https://www.youtube.com/watch?v={video_id}\n\n")
                f.write("## Transcript\n\n")
                f.write(text)
            print(f"  Saved: {filepath}")
    print(f"Done. {ok} transcripts fetched, {failed} failed.")


if __name__ == "__main__":
    main()
