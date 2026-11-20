import os
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
TK = os.path.join(REPO, "toolkit")
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation

F = "Arial"
HDR = PatternFill("solid", fgColor="1D5FBF")
YEL = PatternFill("solid", fgColor="FFF2CC")
thin = Side(style="thin", color="D9D5CA")
B = Border(left=thin, right=thin, top=thin, bottom=thin)

cols = ["#", "Created", "Planned post date", "Format", "Title / Hook", "Topic key", "Companies / entities",
        "Pillar", "Key facts used", "Status", "Posted? (fill in)", "Delivered in"]

rows = [
 # created, planned, format, hook, topic, entities, pillar, facts, status, file
 ("2026-11-05", "", "Text post", "19,000 of you.", "Follower milestone (19K)", "—", "Career & lessons", "20+ years building teams; 'most engineering problems aren't engineering problems'", "Drafted", "Chat"),
 ("2026-11-05", "2026-11-06", "Text + photo", "I spent this week at ADIPEC in Abu Dhabi.", "ADIPEC 2026 / industrial AI", "ADIPEC, ADNOC (context only)", "AI in UAE Industry", "239,000 attendees; 75% increasing AI investment vs ~25% seeing sustained value (Accenture)", "Drafted", "Chat"),
 ("2026-11-10", "", "Text post", "4 rides. Out of 320 million.", "Uber AI agent bookings", "Uber", "Jagged Intelligence", "4 agent rides in a quarter; ~500 Eats orders; ~320M rides/orders", "Drafted", "AI_Case_Study_LinkedIn_Posts.docx"),
 ("2026-11-10", "", "Text post", "1 engineer. A team of AI agents. 10 weeks.", "OpenAI Pando Git rebuild", "OpenAI", "AI-Native Engineering Orgs", "Push latency -80%; 99.99% merge reliability; ~1PB/day", "Drafted", "AI_Case_Study_LinkedIn_Posts.docx"),
 ("2026-11-10", "", "Text post", "America's biggest banks just locked the door on AI agents.", "Banks restrict third-party agents (Oct)", "JPMorgan, BofA, Morgan Stanley, Wells Fargo, Citi", "AI-Native Engineering Orgs", "Agents logging in with customer credentials; read-only moves", "Drafted", "AI_Case_Study_LinkedIn_Posts.docx"),
 ("2026-11-10", "", "Text post", "\"This is the last year we hire engineers.\"", "Proton CTO / AI-written code", "Proton, Jellyfish", "Engineering Leadership", "90% of October code AI-generated; AI coding spend 10x", "Drafted", "AI_Case_Study_LinkedIn_Posts.docx"),
 ("2026-11-10", "", "Text post", "The most valuable AI isn't a chatbot. It's this.", "General Mills logistics AI", "General Mills", "AI-Native Engineering Orgs", "5,000+ shipments/day; $20M+ savings", "Drafted", "AI_Case_Study_LinkedIn_Posts.docx"),
 ("2026-11-10", "", "Newsletter article", "Klarna Replaced 700 Agents With AI. Then It Called Humans Back.", "Klarna AI customer service reversal", "Klarna", "Jagged Intelligence", "2/3 of chats month one; 2.3M conversations; Handoff Map framework", "Drafted", "Klarna_AI_Case_Study_Article.docx"),
 ("2026-11-13", "", "Text post", "A $5 trillion company. 60 direct reports. No successor.", "Nvidia CEO resignation / succession", "Nvidia, Jensen Huang", "Engineering Leadership", "~60 direct reports; ~$500B value lost; first-ever board chair", "Drafted", "AI_Case_Study_Posts_Set2.docx"),
 ("2026-11-13", "", "Text post", "They replaced people with AI. Then asked them back. At higher pay.", "AI rebounding", "SHL, Robert Half, Challenger", "Jagged Intelligence", "19.1% asked back; 51% wanted pay rise; 32% of managers rehired; 121,401 AI job cuts", "Drafted", "AI_Case_Study_Posts_Set2.docx"),
 ("2026-11-13", "", "Text post", "United just banned AI agents from booking flights. Even with your approval.", "United bans AI agent bookings", "United Airlines", "AI-Native Engineering Orgs", "Contract of carriage change 11 Nov; 'another middleman' quote", "Drafted", "AI_Case_Study_Posts_Set2.docx"),
 ("2026-11-13", "", "Text post", "1% of companies drive 80% of the AI spend.", "Ramp AI Index spend concentration", "Ramp, OpenAI, Anthropic", "AI-Native Engineering Orgs", "Top 1% ~80% of spend; $9,500 vs $16 per employee/month", "Drafted", "AI_Case_Study_Posts_Set2.docx"),
 ("2026-11-13", "", "Text post", "Give everyone their own AI agent. Watch the team get worse.", "Multi-agent teams research", "'Worse Together' paper", "Jagged Intelligence", "5 models, 77 scenarios; one agent per person worse everywhere", "Drafted", "AI_Case_Study_Posts_Set2.docx"),
 ("2026-11-13", "", "Newsletter article", "Nvidia Lost $500 Billion in a Week. The Real Failure Wasn't One Man.", "Nvidia key-person risk (article)", "Nvidia", "Engineering Leadership", "Key-Person Test (7 questions)", "Drafted", "Nvidia_Leadership_Article.docx"),
 ("2026-11-17", "", "Carousel (template sample)", "Klarna replaced 700 agents with AI. Then it called humans back.", "Klarna (carousel template sample)", "Klarna", "Jagged Intelligence", "Same as Klarna article", "Template only", "Design canvas"),
 ("2026-11-17", "", "Carousel (6 slides)", "Nvidia's CEO resigned. The $5 trillion company had no plan B.", "Nvidia CEO resignation / succession", "Nvidia", "Engineering Leadership", "$500B; ~60 reports; 'hoping' quote", "Delivered", "Carousel_1_Nvidia_No_Plan_B.pdf"),
 ("2026-11-17", "", "Carousel (6 slides)", "AI agents can now pay for you. The same week, United banned them.", "ChatGPT Wallet vs United ban", "OpenAI, United, Visa, Mastercard, Amex", "AI-Native Engineering Orgs", "Agent Access Ladder framework", "Delivered", "Carousel_2_AI_Agents_Can_Pay.pdf"),
 ("2026-11-17", "", "Carousel (6 slides)", "They replaced people with AI. Then asked them back. At higher pay.", "AI rebounding", "SHL, Robert Half", "Jagged Intelligence", "Rebound Test framework", "Delivered", "Carousel_3_AI_Rebounding.pdf"),
 ("2026-11-18", "2026-11-19", "Carousel (6 slides)", "Anthropic goes public today. The real story isn't the $1.4 trillion.", "Anthropic IPO governance lessons", "Anthropic", "Engineering Leadership", "$33.2B revenue 9M; trust elects 3 of 5 directors; 50.1% founder votes", "Delivered", "Carousel_4_Anthropic_IPO_Leadership_Lessons.pdf"),
 ("2026-11-19", "2026-11-20 09:00", "Text + image", "Your AI agent got hacked. Your bank says that's your problem.", "Banks shift AI agent losses to customers", "Citi, PNC, Citizens, Wells Fargo, JPMorgan", "AI-Native Engineering Orgs", "New terms Nov 2026; Wells Fargo effective 24 Nov", "Scheduled in Buffer", "Buffer"),
 ("2026-11-19", "2026-11-23 08:45", "Text + image", "\"Greater AI autonomy requires greater transparency.\"", "Microsoft AI Transparency Initiative", "Microsoft, Accenture, Adobe, KPMG, Mastercard, Volvo Cars", "AI-Native Engineering Orgs", "40+ orgs; See / Verify / Control", "Scheduled in Buffer", "Buffer"),
 ("2026-11-19", "2026-11-24 15:30", "Text + image", "$4.5 billion. For a company that helps businesses run their own AI models.", "Palo Alto buys Applied Compute", "Palo Alto Networks, Applied Compute", "AI-Native Engineering Orgs", "$4.5B all-stock; Arora quote", "Scheduled in Buffer", "Buffer"),
 ("2026-11-19", "2026-11-25 16:00", "Text + image", "The new model is smarter. It's also twice as likely to hide that it failed.", "GPT-6.2 Astra hides coding failures", "OpenAI", "Jagged Intelligence", "22.28% vs 11.09% blocker omission; 23% vs 7.58%", "Scheduled in Buffer", "Buffer"),
 ("2026-11-19", "2026-11-26 16:30", "Text + image", "4 AI stories. 1 lesson every engineering leader needs.", "Week wrap: AI accountability", "(recap of the four above)", "Engineering Leadership", "Identity / Evidence / Approval / Ownership", "Scheduled in Buffer", "Buffer"),
 ("2026-11-19", "2026-11-27 09:00", "Video (32s, vertical) + caption", "Same AI tools. Brilliant in one team. Stuck in the next.", "Adecco Global Workforce study: people-led AI adoption", "The Adecco Group", "Engineering Leadership", "40,500 workers/36 countries; 96% vs 29% willing to adapt; 92% vs 15% comfortable; 93% vs 47% productive; training 77%→67%", "Scheduled in Buffer", "Buffer + videos/01-jagged-edge-people-not-tools.mp4"),
 ("2026-11-19", "2026-11-30 08:45", "Video (31s, vertical) + caption", "AI tools change every few months. The stack doesn't.", "Students: learn the AI engineering stack, not tools", "—", "Career & lessons", "6 layers: Python+SQL, Data, ML, LLMs, Evaluation (most skipped), Deployment; music: bright piano", "Scheduled in Buffer", "Buffer + videos/02-learn-the-stack-not-the-tool.mp4"),
 ("2026-11-19", "2026-12-01 15:30", "Video (29s, vertical) + caption", "In tutorials, AI works first time. In production, it fails quietly.", "Students: production lessons tutorials skip", "—", "Career & lessons", "5 lessons: data drift, edge cases, cost per request, silent failures, human handoff; music: lo-fi Rhodes", "Scheduled in Buffer", "Buffer + videos/03-what-production-teaches-you.mp4"),
 ("2026-11-19", "2026-12-03 16:30", "Video (31s, vertical) + caption", "Most AI portfolios look the same. Here's how to stand out.", "Students: AI portfolio projects that get remembered", "—", "Career & lessons", "5 steps: real problem, baseline, simplest version, numbers (accuracy/latency/cost), show failures; README checklist; music: marimba", "Scheduled in Buffer", "Buffer + videos/04-ai-project-recruiters-remember.mp4"),
 ("2026-11-19", "2026-12-04 09:00", "Video (32s, vertical) + caption", "Your LLM demo is 1 box. Production is 7.", "Students: architecture of a production LLM app", "—", "Design & architecture", "7 boxes: App/API, input guardrails, retrieval, LLM, output checks, logging+eval, human fallback; 4 catch failures; music: ambient bell", "Scheduled in Buffer", "Buffer + videos/05-how-a-production-llm-app-is-built.mp4"),
]

wb = Workbook()
ws = wb.active
ws.title = "Content Log"
ws.append(cols)
for i, r in enumerate(rows, 1):
    ws.append([i, r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], "", r[9]])

widths = [5, 12, 18, 20, 58, 36, 34, 26, 52, 20, 16, 40]
for i, w in enumerate(widths, 1):
    ws.column_dimensions[ws.cell(1, i).column_letter].width = w
for c in ws[1]:
    c.font = Font(name=F, bold=True, color="FFFFFF"); c.fill = HDR
    c.alignment = Alignment(vertical="center", wrap_text=True); c.border = B
ws.row_dimensions[1].height = 30
for row in ws.iter_rows(min_row=2):
    for c in row:
        c.font = Font(name=F, size=10); c.alignment = Alignment(vertical="top", wrap_text=True); c.border = B
    row[4].font = Font(name=F, size=10, bold=True)
    row[10].fill = YEL
ws.freeze_panes = "F2"
ws.auto_filter.ref = ws.dimensions
dv = DataValidation(type="list", formula1='"Yes,No,Skipped"', allow_blank=True)
ws.add_data_validation(dv); dv.add(f"K2:K{len(rows)+200}")

# Ideas backlog
ib = wb.create_sheet("Ideas Backlog")
ib.append(["Idea", "Why it could work", "Source / date", "Verification status"])
ideas = [
 ("Agent harness matters more than the model (FrontierHarness)", "64.5% of spend on failed runs; same model, 1.8–5x cost difference", "Bitdoze digest, 18 Nov 2026", "Re-verify before use"),
 ("'The agent is only as good as the evidence loop'", "~90% of Claude Code's code written and reviewed by AI; testing as the safety net", "Bitdoze digest, 18 Nov 2026", "Read original post first"),
 ("AI agents arrive in the bond market", "First agent-executed bond trades (Microsoft bond)", "Bloomberg, 17 Nov 2026", "Paywalled; confirm details"),
 ("Coinbase AI blocks $4.7M deepfake scam", "AI vs AI fraud; 91% of transfers blocked", "BleepingComputer via AI Weekly, 19 Nov 2026", "Not yet verified"),
 ("AI-designed chip circuits (OpenAI)", "AI redesign cut chip area ~15%", "OpenAI via The Neuron, 19 Nov 2026", "Not yet verified"),
 ("Anthropic IPO aftermath", "Priced $83, ~$81B raised, opened $111.50 (largest US IPO)", "Renaissance Capital, CNN, 19 Nov 2026", "Verified; avoid repeating carousel angle"),
]
for r in ideas: ib.append(list(r))
for i, w in enumerate([52, 60, 40, 30], 1):
    ib.column_dimensions[ib.cell(1, i).column_letter].width = w
for c in ib[1]:
    c.font = Font(name=F, bold=True, color="FFFFFF"); c.fill = HDR; c.border = B
for row in ib.iter_rows(min_row=2):
    for c in row:
        c.font = Font(name=F, size=10); c.alignment = Alignment(vertical="top", wrap_text=True); c.border = B
ib.freeze_panes = "A2"

# How to use
hu = wb.create_sheet("How to use")
lines = [
 "How to use this log",
 "",
 "1. Before writing new content, check the 'Topic key' and 'Companies / entities' columns. Don't repeat a topic unless there is genuinely new news on it.",
 "2. Research only the previous 7 days of AI news for each new week.",
 "3. After writing new posts, add one row per post or article at the bottom of 'Content Log'.",
 "4. Yellow column 'Posted? (fill in)': choose Yes / No / Skipped once each item goes live.",
 "5. 'Ideas Backlog' holds researched topics not yet used. Re-verify before using; most go stale after a week.",
 "",
 "Example row format: Created 2026-11-19 · Planned 2026-11-20 09:00 · Text + image · hook in quotes if it is a quote · short topic key.",
]
for l in lines: hu.append([l])
hu.column_dimensions["A"].width = 120
hu["A1"].font = Font(name=F, bold=True, size=14, color="1D5FBF")
for r in hu.iter_rows(min_row=2):
    for c in r: c.font = Font(name=F, size=11); c.alignment = Alignment(wrap_text=True)

wb.save(os.path.join(REPO, "logs", "Vevek_LinkedIn_Content_Log.xlsx"))

# Markdown copy for the project
md = ["# Vevek LinkedIn content log", "", "Check this before writing new posts. Do not repeat a topic key unless there is genuinely new news. Research only the previous 7 days.", "",
      "| # | Created | Planned | Format | Title / Hook | Topic key | Pillar | Status |", "|---|---|---|---|---|---|---|---|"]
for i, r in enumerate(rows, 1):
    md.append(f"| {i} | {r[0]} | {r[1]} | {r[2]} | {r[3].replace('|','/')} | {r[4]} | {r[6]} | {r[8]} |")
md += ["", "## Ideas backlog (researched, not yet used; re-verify before use)", ""]
for r in ideas: md.append(f"- **{r[0]}**: {r[1]} ({r[2]}; {r[3]})")
open(os.path.join(REPO, "logs", "linkedin-content-log.md"), "w").write("\n".join(md) + "\n")
print(len(rows), "rows")
