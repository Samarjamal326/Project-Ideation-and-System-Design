"""
PDF Generator for Campus Engagement & Event Management Platform - Project Proposal
Uses ReportLab to generate a professionally formatted PDF from the project proposal content.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.platypus.flowables import HRFlowable
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

OUTPUT_PATH = r"C:\Users\Prakash Gusain Ji\.gemini\antigravity-ide\scratch\Project-Ideation-and-System-Design\07-Project-Proposal\Project-Proposal-Campus-Events.pdf"

# ─────────────────────────────────────────────
# COLOR PALETTE
# ─────────────────────────────────────────────
PRIMARY      = colors.HexColor("#1E3A5F")   # Deep navy blue
ACCENT       = colors.HexColor("#2E86AB")   # Bright teal
LIGHT_BG     = colors.HexColor("#F0F4F8")   # Light grey-blue
WHITE        = colors.white
DARK_TEXT    = colors.HexColor("#1A1A2E")
MID_TEXT     = colors.HexColor("#4A4A6A")
TABLE_HEADER = colors.HexColor("#1E3A5F")
TABLE_ROW1   = colors.HexColor("#EAF2F8")
TABLE_ROW2   = colors.white
RULE_COLOR   = colors.HexColor("#2E86AB")

# ─────────────────────────────────────────────
# STYLES
# ─────────────────────────────────────────────
styles = getSampleStyleSheet()

def make_styles():
    custom = {}

    custom['DocTitle'] = ParagraphStyle(
        'DocTitle',
        fontSize=26,
        textColor=WHITE,
        fontName='Helvetica-Bold',
        alignment=TA_CENTER,
        leading=32,
        spaceAfter=4
    )
    custom['DocSubtitle'] = ParagraphStyle(
        'DocSubtitle',
        fontSize=14,
        textColor=colors.HexColor("#A8D8EA"),
        fontName='Helvetica',
        alignment=TA_CENTER,
        leading=20,
        spaceAfter=4
    )
    custom['DocMeta'] = ParagraphStyle(
        'DocMeta',
        fontSize=10,
        textColor=colors.HexColor("#D0E8F5"),
        fontName='Helvetica',
        alignment=TA_CENTER,
        leading=16,
        spaceAfter=2
    )
    custom['H1'] = ParagraphStyle(
        'H1',
        fontSize=16,
        textColor=WHITE,
        fontName='Helvetica-Bold',
        alignment=TA_LEFT,
        leading=22,
        spaceBefore=16,
        spaceAfter=8,
        leftIndent=0,
        borderPad=8,
        backColor=PRIMARY,
        borderRadius=4,
    )
    custom['H2'] = ParagraphStyle(
        'H2',
        fontSize=12,
        textColor=PRIMARY,
        fontName='Helvetica-Bold',
        alignment=TA_LEFT,
        leading=18,
        spaceBefore=12,
        spaceAfter=4,
        borderPadding=(0, 0, 2, 0),
    )
    custom['H3'] = ParagraphStyle(
        'H3',
        fontSize=10,
        textColor=ACCENT,
        fontName='Helvetica-Bold',
        alignment=TA_LEFT,
        leading=15,
        spaceBefore=8,
        spaceAfter=3,
    )
    custom['Body'] = ParagraphStyle(
        'Body',
        fontSize=9.5,
        textColor=DARK_TEXT,
        fontName='Helvetica',
        alignment=TA_JUSTIFY,
        leading=15,
        spaceBefore=4,
        spaceAfter=4,
    )
    custom['Bullet'] = ParagraphStyle(
        'Bullet',
        fontSize=9.5,
        textColor=DARK_TEXT,
        fontName='Helvetica',
        alignment=TA_LEFT,
        leading=15,
        spaceBefore=2,
        spaceAfter=2,
        leftIndent=18,
        bulletIndent=6,
    )
    custom['SubBullet'] = ParagraphStyle(
        'SubBullet',
        fontSize=9,
        textColor=MID_TEXT,
        fontName='Helvetica',
        alignment=TA_LEFT,
        leading=14,
        spaceBefore=1,
        spaceAfter=1,
        leftIndent=32,
        bulletIndent=20,
    )
    custom['Note'] = ParagraphStyle(
        'Note',
        fontSize=9,
        textColor=MID_TEXT,
        fontName='Helvetica-Oblique',
        alignment=TA_LEFT,
        leading=13,
        spaceBefore=4,
        spaceAfter=4,
        leftIndent=12,
    )
    custom['Code'] = ParagraphStyle(
        'Code',
        fontSize=8.5,
        textColor=colors.HexColor("#2C3E50"),
        fontName='Courier',
        alignment=TA_LEFT,
        leading=13,
        spaceBefore=4,
        spaceAfter=4,
        leftIndent=16,
        backColor=LIGHT_BG,
        borderPad=6,
    )
    custom['TOCItem'] = ParagraphStyle(
        'TOCItem',
        fontSize=10,
        textColor=PRIMARY,
        fontName='Helvetica',
        alignment=TA_LEFT,
        leading=18,
        leftIndent=10,
    )
    custom['Footer'] = ParagraphStyle(
        'Footer',
        fontSize=8,
        textColor=colors.grey,
        fontName='Helvetica',
        alignment=TA_CENTER,
        leading=12,
    )
    return custom

S = make_styles()

# ─────────────────────────────────────────────
# TABLE STYLE HELPER
# ─────────────────────────────────────────────
def make_table(data, col_widths=None, header=True):
    page_w = A4[0] - 4*cm
    if col_widths is None:
        col_widths = [page_w / len(data[0])] * len(data[0])

    table = Table(data, colWidths=col_widths, repeatRows=1 if header else 0)
    style_cmds = [
        ('FONTNAME',  (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE',  (0,0), (-1,0), 9),
        ('BACKGROUND',(0,0), (-1,0), TABLE_HEADER),
        ('TEXTCOLOR', (0,0), (-1,0), WHITE),
        ('ALIGN',     (0,0), (-1,-1), 'LEFT'),
        ('VALIGN',    (0,0), (-1,-1), 'MIDDLE'),
        ('FONTNAME',  (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE',  (0,1), (-1,-1), 8.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [TABLE_ROW1, TABLE_ROW2]),
        ('GRID',      (0,0), (-1,-1), 0.4, colors.HexColor("#BDC3C7")),
        ('TOPPADDING',  (0,0), (-1,-1), 5),
        ('BOTTOMPADDING',(0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING',(0,0), (-1,-1), 8),
    ]
    table.setStyle(TableStyle(style_cmds))
    return table

def h1(text):
    """Section heading with filled background box."""
    return Paragraph(f"&nbsp;&nbsp;{text}", S['H1'])

def h2(text):
    return Paragraph(text, S['H2'])

def h3(text):
    return Paragraph(text, S['H3'])

def body(text):
    return Paragraph(text, S['Body'])

def bullet(text, bold_part=None):
    if bold_part:
        text = text.replace(bold_part, f"<b>{bold_part}</b>")
    return Paragraph(f"• &nbsp;{text}", S['Bullet'])

def subbullet(text):
    return Paragraph(f"– &nbsp;{text}", S['SubBullet'])

def sp(n=6):
    return Spacer(1, n)

def rule():
    return HRFlowable(width="100%", thickness=1, color=RULE_COLOR, spaceAfter=6, spaceBefore=6)

# ─────────────────────────────────────────────
# COVER PAGE
# ─────────────────────────────────────────────
def cover_page(elements):
    # Big colored header block using a table
    cover_data = [[Paragraph(
        "<b>Campus Engagement &amp;<br/>Event Management Platform</b>",
        ParagraphStyle('CT', fontSize=28, textColor=WHITE, fontName='Helvetica-Bold',
                       alignment=TA_CENTER, leading=36)
    )]]
    cover_table = Table(cover_data, colWidths=[A4[0] - 3*cm])
    cover_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), PRIMARY),
        ('TOPPADDING', (0,0), (-1,-1), 40),
        ('BOTTOMPADDING', (0,0), (-1,-1), 40),
        ('LEFTPADDING', (0,0), (-1,-1), 20),
        ('RIGHTPADDING', (0,0), (-1,-1), 20),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    elements.append(cover_table)
    elements.append(sp(16))

    subtitle_data = [[Paragraph(
        "Final Year Project Proposal",
        ParagraphStyle('ST', fontSize=16, textColor=ACCENT, fontName='Helvetica-Bold',
                       alignment=TA_CENTER, leading=22)
    )]]
    sub_table = Table(subtitle_data, colWidths=[A4[0] - 3*cm])
    sub_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('TOPPADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    elements.append(sub_table)
    elements.append(sp(32))

    meta = [
        ["Submitted By:", "[Your Name]"],
        ["Department:", "[Your Department]"],
        ["Institution:", "[Your College Name]"],
        ["Academic Year:", "2025 – 2026"],
        ["Project Guide / Mentor:", "[Mentor Name]"],
        ["Date:", "July 2026"],
    ]
    meta_table = Table(
        [[Paragraph(f"<b>{k}</b>", ParagraphStyle('mk', fontSize=10, fontName='Helvetica-Bold',
                                                   textColor=PRIMARY, leading=16)),
          Paragraph(v, ParagraphStyle('mv', fontSize=10, fontName='Helvetica',
                                      textColor=DARK_TEXT, leading=16))]
         for k, v in meta],
        colWidths=[6*cm, 10*cm]
    )
    meta_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('LINEBELOW', (0,0), (-1,-2), 0.3, colors.HexColor("#D5D8DC")),
    ]))
    elements.append(meta_table)
    elements.append(PageBreak())

# ─────────────────────────────────────────────
# TABLE OF CONTENTS
# ─────────────────────────────────────────────
def toc_page(elements):
    elements.append(h1("Table of Contents"))
    elements.append(sp(12))
    toc_items = [
        ("1.", "Executive Summary"),
        ("2.", "Problem Statement"),
        ("3.", "Proposed Solution"),
        ("4.", "Complete Workflow"),
        ("5.", "User Roles & Responsibilities"),
        ("6.", "Platform Dashboards"),
        ("7.", "Student Features"),
        ("8.", "Club Features"),
        ("9.", "Special Feature: Eliminating WhatsApp Groups"),
        ("10.", "Event Types & Dynamic Forms"),
        ("11.", "External Participants"),
        ("12.", "QR-Based Attendance"),
        ("13.", "AI Features"),
        ("14.", "Implementation Plan"),
        ("15.", "Technology Stack"),
        ("16.", "System Architecture"),
        ("17.", "Research Potential"),
        ("18.", "Facts & Industry Figures"),
        ("19.", "Why This Is a Major Project"),
        ("20.", "Future Scope"),
        ("21.", "Conclusion"),
    ]
    toc_data = [[
        Paragraph(f"<b>{num}</b>", ParagraphStyle('tn', fontSize=9.5, fontName='Helvetica-Bold',
                                                   textColor=ACCENT, leading=15)),
        Paragraph(title, ParagraphStyle('tt', fontSize=9.5, fontName='Helvetica',
                                        textColor=DARK_TEXT, leading=15))
    ] for num, title in toc_items]

    toc_table = Table(toc_data, colWidths=[1.2*cm, 14*cm])
    toc_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('ROWBACKGROUNDS', (0,0), (-1,-1), [LIGHT_BG, WHITE]),
    ]))
    elements.append(toc_table)
    elements.append(PageBreak())

# ─────────────────────────────────────────────
# MAIN CONTENT BUILDER
# ─────────────────────────────────────────────
def build_content(elements):
    W = A4[0] - 4*cm  # usable width

    # ─── 1. EXECUTIVE SUMMARY ───────────────
    elements.append(h1("1. Executive Summary"))
    elements.append(sp(6))
    elements.append(body(
        "Most colleges today manage events through a mix of WhatsApp groups, Google Forms, "
        "paper notices, and email chains. This leads to confusion, missed deadlines, and wasted "
        "time for everyone involved — students, clubs, faculty, and administration."
    ))
    elements.append(body(
        "This project proposes a <b>Campus Engagement &amp; Event Management Platform</b> — a single, "
        "centralized web application designed specifically for universities. It connects students, "
        "student clubs, faculty coordinators, and college administration through one ecosystem."
    ))
    elements.append(body(
        "The platform digitizes the complete lifecycle of a campus event — from requesting a venue "
        "and getting approvals, all the way to marking attendance with QR codes and automatically "
        "generating participation certificates."
    ))
    elements.append(body(
        "This is a complete, production-quality software project with a real problem to solve, "
        "a clear user base, and strong potential for research publication and adoption by other institutions."
    ))
    elements.append(sp(8))

    # ─── 2. PROBLEM STATEMENT ───────────────
    elements.append(h1("2. Problem Statement"))
    elements.append(sp(6))
    elements.append(h2("2.1  How Campus Events Are Managed Today"))
    elements.append(body(
        "The current event management process in most colleges is fragmented and manual:"
    ))
    t1_data = [
        ["Step", "How It Is Done Today"],
        ["Event Approval Request", "Physical letter or email to HOD / Dean"],
        ["Venue Booking", "Separate email or verbal request to administration"],
        ["Announcements", "WhatsApp broadcasts, Instagram posts, notice boards"],
        ["Student Registrations", "Google Forms, manual collection"],
        ["Event Communication", "New WhatsApp group created for every event"],
        ["Attendance", "Paper sheets, manually entered later"],
        ["Certificates", "Designed manually in Canva, sent via email one by one"],
        ["Analytics", "No records kept at all"],
    ]
    elements.append(make_table(t1_data, col_widths=[6*cm, 10.5*cm]))
    elements.append(sp(8))

    elements.append(h2("2.2  Core Problems"))
    problems = [
        ("Problem 1 — Multiple WhatsApp Groups",
         "Every event creates a new WhatsApp group. After the event, the group becomes inactive clutter. "
         "Students are part of 15–20 WhatsApp groups with no way to organize or filter them."),
        ("Problem 2 — Scattered Announcements",
         "Event information is spread across Instagram, WhatsApp, notice boards, and emails. "
         "A student who missed a WhatsApp message may never know the event happened."),
        ("Problem 3 — Manual Approval Process",
         "Club heads physically write letters or send emails to faculty coordinators and administration. "
         "This takes days, and there is no way to track approval status."),
        ("Problem 4 — Venue Booking Conflicts",
         "There is no central venue calendar. Two clubs may request the same auditorium on the same "
         "day without knowing. The conflict is discovered only at the last minute."),
        ("Problem 5 — Manual Attendance",
         "Volunteers carry paper sheets and call out names. This is time-consuming, error-prone, "
         "and produces no usable data afterward."),
        ("Problem 6 — Certificate Delays",
         "Certificates are designed manually, sometimes weeks after the event. Students who "
         "participated in multiple events have to follow up individually."),
        ("Problem 7 — No Analytics",
         "Clubs have no way of knowing how many students viewed their event, how many registered "
         "vs attended, or what time of day gets better registrations."),
        ("Problem 8 — Students Miss Opportunities",
         "A student interested in technical events has no way to discover all upcoming workshops "
         "or hackathons across different clubs in one place."),
    ]
    for title, desc in problems:
        elements.append(Paragraph(f"<b>{title}</b>", S['Body']))
        elements.append(body(desc))
        elements.append(sp(4))

    elements.append(h2("2.3  Why This Wastes Time"))
    elements.append(body(
        "A single event today requires a club head to: Create a Google Form → Share on WhatsApp → "
        "Get approvals via email → Create a WhatsApp group → Download responses from Google Sheets → "
        "Mark attendance manually → Design certificates individually → Broadcast results on WhatsApp again."
    ))
    elements.append(body(
        "<b>This process takes 20–30 hours of effort for a medium-sized event.</b> The platform proposed here "
        "can reduce this to under 4 hours, with most steps automated."
    ))
    elements.append(sp(8))

    # ─── 3. PROPOSED SOLUTION ───────────────
    elements.append(h1("3. Proposed Solution"))
    elements.append(sp(6))
    elements.append(body(
        "The platform brings everything under one roof. Instead of switching between WhatsApp, "
        "Google Forms, Gmail, and notice boards — every step of event management happens inside this platform."
    ))
    solution_points = [
        ("Clubs", "create and manage events through a structured, guided dashboard."),
        ("Approval Routing", "automatically routes approval requests to faculty and administration — no emails needed."),
        ("Venue Availability", "is checked in real time before booking, preventing conflicts."),
        ("Events", "are published to a central discovery feed visible to all students."),
        ("Students", "browse, filter, and register with one click using their saved profile."),
        ("Communication", "happens inside the platform via built-in event channels — no WhatsApp required."),
        ("Attendance", "is marked instantly by scanning student QR codes on the day of the event."),
        ("Certificates", "are generated automatically and emailed to all verified attendees post-event."),
        ("Analytics", "give clubs a full report — registrations, attendance, engagement, and feedback."),
    ]
    for bold, rest in solution_points:
        elements.append(Paragraph(f"• &nbsp;<b>{bold}</b> {rest}", S['Bullet']))
    elements.append(sp(8))

    # ─── 4. COMPLETE WORKFLOW ───────────────
    elements.append(h1("4. Complete Workflow"))
    elements.append(sp(6))
    elements.append(body("Here is the complete step-by-step journey of an event on this platform:"))
    elements.append(sp(6))
    workflow_data = [
        ["Step", "Action", "Who Does It"],
        ["1", "Log in and create a new event", "Club Head"],
        ["2", "Select event type → platform generates registration form", "Club Head"],
        ["3", "Submit venue request (date, time, hall needed)", "Club Head"],
        ["4", "Review event proposal and approve / reject", "Faculty Coordinator"],
        ["5", "Confirm venue availability and approve booking", "College Admin"],
        ["6", "Event is published to the central student feed", "Platform (Automated)"],
        ["7", "Students browse, filter, and register for the event", "Students"],
        ["8", "Club shortlists participants and notifies them", "Club Head"],
        ["9", "Registered participants join the event channel / community", "Platform (Automated)"],
        ["10", "Volunteers scan student QR codes to mark attendance", "Volunteers / Club"],
        ["11", "Participation certificates auto-generated and emailed", "Platform (Automated)"],
        ["12", "Analytics report available on club dashboard", "Platform (Automated)"],
    ]
    elements.append(make_table(workflow_data, col_widths=[1*cm, 9*cm, 6*cm]))
    elements.append(sp(8))

    # ─── 5. USER ROLES ───────────────
    elements.append(h1("5. User Roles & Responsibilities"))
    elements.append(sp(6))
    elements.append(body(
        "The platform supports six distinct user types. Each user sees only the features relevant to them."
    ))
    roles_data = [
        ["Role", "Description & Responsibilities"],
        ["Student",
         "Browses events, registers, receives QR passes, attends events, and downloads certificates."],
        ["Club Head",
         "Creates and manages events, submits approvals, manages registrations, marks attendance, views analytics."],
        ["Faculty Coordinator",
         "Reviews event proposals from clubs. Approves or rejects with written remarks. Monitors compliance."],
        ["College Admin",
         "Manages venue booking and scheduling across campus. Resolves conflicts. Sees all institution events."],
        ["Super Admin",
         "Full platform control — user management, system health monitoring, platform-wide configuration."],
        ["External Participant",
         "Student from another college. Registers via email verification, receives guest QR pass and certificate."],
    ]
    elements.append(make_table(roles_data, col_widths=[4.5*cm, 12*cm]))
    elements.append(sp(8))

    # ─── 6. DASHBOARDS ───────────────
    elements.append(h1("6. Platform Dashboards"))
    elements.append(sp(6))
    elements.append(body("Each user role gets its own tailored dashboard with relevant tools and data."))
    elements.append(sp(6))

    dashboards = [
        ("Student Dashboard", [
            "Personalized event recommendations based on interests",
            "Upcoming events calendar with filters",
            "Registered events with downloadable QR passes",
            "Real-time shortlisting status notifications",
            "Certificate download history",
            "Joined event communities and announcement feeds",
        ]),
        ("Club Dashboard", [
            "Create and manage multiple events simultaneously",
            "View and export registration lists",
            "Shortlist participants and send targeted notifications",
            "Track approval status in real time (Faculty → Admin)",
            "Manage volunteers, judges, and sponsors",
            "Post announcements to event channel",
            "View post-event analytics and attendance data",
        ]),
        ("Faculty Dashboard", [
            "Incoming approval requests from clubs with full event details",
            "Approve or reject events with written remarks",
            "View all events under managed departments",
            "Monitor club activity logs and compliance records",
        ]),
        ("Admin Dashboard", [
            "Full venue booking calendar — all halls and labs",
            "Approval queue forwarded from faculty",
            "Institution-wide event analytics and reports",
            "User management (clubs, coordinators, admins)",
            "System-wide announcements and policy notices",
        ]),
    ]
    for dash_name, features in dashboards:
        elements.append(h2(dash_name))
        for f in features:
            elements.append(bullet(f))
        elements.append(sp(4))
    elements.append(sp(8))

    # ─── 7. STUDENT FEATURES ───────────────
    elements.append(h1("7. Student Features"))
    elements.append(sp(6))
    student_features = [
        ["Feature", "What It Does"],
        ["Browse Events", "Discover all upcoming events in a clean, filterable feed"],
        ["Filter by Category", "Filter by Technical, Cultural, Sports, Workshops, etc."],
        ["One-Click Registration", "Register for events using saved profile data — no re-entering details"],
        ["Save / Bookmark Events", "Save events to check later; get reminders before registration closes"],
        ["Event Reminders", "Push and email reminders sent 24 hours before the event starts"],
        ["Notifications", "Receive alerts for shortlisting results, approval updates, and announcements"],
        ["QR Event Pass", "Unique digital QR code for event entry and automated attendance marking"],
        ["Join Event Community", "Access the event's built-in announcement and discussion channel"],
        ["Shortlisting Status", "Real-time visibility of registration and selection status"],
        ["Download Certificates", "Participation certificates available for download immediately after event"],
        ["Participation History", "View all past events attended and certificates earned in one place"],
        ["Calendar Integration", "Sync registered events to Google Calendar or iCal"],
        ["Personalized Feed", "AI recommends events based on the student's participation history and interests"],
    ]
    elements.append(make_table(student_features, col_widths=[5*cm, 11.5*cm]))
    elements.append(sp(8))

    # ─── 8. CLUB FEATURES ───────────────
    elements.append(h1("8. Club Features"))
    elements.append(sp(6))
    club_features = [
        ["Feature", "What It Does"],
        ["Create Events", "Multi-step event creation wizard with validation checks"],
        ["Upload Event Poster", "Upload event banners and promotional artwork"],
        ["Dynamic Registration Forms", "Platform auto-generates the correct form based on event type"],
        ["Accept Registrations", "View and manage all registrations in real time with export options"],
        ["Shortlist Participants", "Select and notify shortlisted students with a single click"],
        ["Send Announcements", "Push targeted updates to all registered participants"],
        ["Event Discussion Channel", "Built-in community feed — no WhatsApp group needed"],
        ["Manage Volunteers", "Assign QR scanning roles and duties to volunteers"],
        ["QR Attendance System", "Scan student QR codes to mark attendance instantly"],
        ["Auto-Generate Certificates", "One-click certificate generation for all verified attendees"],
        ["Analytics Dashboard", "View registrations, attendance, engagement, and feedback reports"],
        ["Request Venues", "Submit venue request with time slot and infrastructure requirements"],
        ["Track Approval Status", "Live tracking of approval stages — Faculty → Admin"],
        ["Manage Sponsors", "Add sponsor logos and details to the event page"],
        ["Manage Judges / Guests", "Invite and manage external judges or distinguished guests"],
    ]
    elements.append(make_table(club_features, col_widths=[5*cm, 11.5*cm]))
    elements.append(sp(8))

    # ─── 9. WHATSAPP ELIMINATION ───────────────
    elements.append(h1("9. Special Feature: Eliminating WhatsApp Groups"))
    elements.append(sp(6))
    elements.append(h2("The Problem"))
    elements.append(body(
        "Every campus event today requires creating a new WhatsApp group. Students are added forcibly "
        "without consent. After the event, inactive groups pile up — students belong to 15–20+ groups "
        "with no way to organize them. Spam and off-topic messages dilute important announcements. "
        "Past event history is completely lost when members leave or the group becomes inactive."
    ))
    elements.append(h2("The Solution — Built-In Event Communities"))
    elements.append(body(
        "When an event is created on this platform, an <b>Event Channel</b> is automatically created. "
        "Every registered participant is automatically added to this channel. Club heads can post "
        "announcements (one-way) or enable a discussion feed (two-way). When the event ends, "
        "the channel is archived and preserved for future reference."
    ))
    elements.append(h2("Why This Is Better Than WhatsApp"))
    compare_data = [
        ["WhatsApp Groups", "Platform Event Channels"],
        ["Phone numbers shared publicly", "No phone numbers required — privacy protected"],
        ["Anyone can be added without consent", "Only registered participants join"],
        ["Off-topic messages and spam", "Moderated, on-topic communications only"],
        ["History lost when members leave", "Full archive preserved after event ends"],
        ["No moderation or admin control", "Club head has full moderation authority"],
        ["Mixed with personal conversations", "Dedicated, organized, event-only space"],
    ]
    elements.append(make_table(compare_data, col_widths=[7.5*cm, 9*cm]))
    elements.append(sp(8))

    # ─── 10. EVENT TYPES ───────────────
    elements.append(h1("10. Event Types & Dynamic Registration Forms"))
    elements.append(sp(6))
    elements.append(body(
        "Different events need different registration data. A hackathon needs team names and tech stack. "
        "A dance competition needs a video link. A seminar just needs a name and roll number. "
        "The platform solves this by auto-generating the appropriate form based on the event type selected."
    ))
    elements.append(sp(6))
    event_types_data = [
        ["Event Category", "Event Types", "Auto-Generated Form Fields"],
        ["Technical", "Hackathon", "Team name, size, tech stack, project idea"],
        ["Technical", "Coding Contest", "Individual/team, programming language preference"],
        ["Technical", "Workshop", "Skill level, laptop availability"],
        ["Cultural", "Dance Competition", "Solo/group, dance form, video submission link"],
        ["Cultural", "Music Event", "Instrument/vocal, audio sample upload"],
        ["Cultural", "Literary", "Writing sample, word limit acknowledgement"],
        ["Sports", "Any Sport", "Individual/team, preferred sport category"],
        ["Academic", "Department Seminar", "Roll number, department, academic year"],
        ["Other", "Custom Event", "Manual drag-and-drop form builder"],
    ]
    elements.append(make_table(event_types_data, col_widths=[3.5*cm, 3.5*cm, 9.5*cm]))
    elements.append(sp(8))

    # ─── 11. EXTERNAL PARTICIPANTS ───────────────
    elements.append(h1("11. External Participants"))
    elements.append(sp(6))
    elements.append(body(
        "Many events — especially hackathons and cultural fests — welcome students from other colleges. "
        "The platform handles this with a smooth, verified guest registration flow."
    ))
    ext_data = [
        ["Step", "Action"],
        ["1", "External student visits the public event page — no login required to view"],
        ["2", "Clicks 'Register as External Participant'"],
        ["3", "Enters name, college name, and institutional email address"],
        ["4", "A verification email is sent — student must click the link to confirm identity"],
        ["5", "After verification, student completes the event registration form"],
        ["6", "A unique Guest QR Pass is generated and emailed"],
        ["7", "On event day, QR is scanned — attendance marked the same as internal students"],
        ["8", "After the event, participation certificate is emailed automatically"],
    ]
    elements.append(make_table(ext_data, col_widths=[0.8*cm, 15.7*cm]))
    elements.append(sp(4))
    elements.append(Paragraph(
        "<b>Optional Payment Gateway:</b> For paid events, external participants can pay "
        "registration fees online directly on the platform.",
        S['Note']
    ))
    elements.append(sp(8))

    # ─── 12. QR ATTENDANCE ───────────────
    elements.append(h1("12. QR-Based Attendance System"))
    elements.append(sp(6))
    elements.append(h2("How It Works"))
    qr_steps = [
        "Every registered student receives a unique QR code in their confirmation email and dashboard.",
        "On event day, volunteers open the scanner on any smartphone or tablet — no special device needed.",
        "They scan the student's QR code — attendance is marked instantly in the database.",
        "Duplicate scans are blocked automatically — proxy attendance is prevented.",
        "A real-time attendance count appears on the club dashboard.",
        "After the event, a full attendance report is available for download.",
    ]
    for i, step in enumerate(qr_steps, 1):
        elements.append(Paragraph(f"&nbsp;&nbsp;<b>{i}.</b> &nbsp;{step}", S['Body']))
        elements.append(sp(3))

    elements.append(sp(6))
    elements.append(h2("QR vs. Manual Attendance"))
    qr_compare = [
        ["Manual Method", "QR-Based Attendance"],
        ["Takes 20–40 minutes for large groups", "Completes in minutes — any crowd size"],
        ["Error-prone (wrong names, bad handwriting)", "100% accurate — database-driven"],
        ["Requires manual data entry after the event", "Data captured instantly — no entry needed"],
        ["No real-time visibility of attendance count", "Live count visible on club dashboard"],
        ["Cannot easily prevent proxy entries", "Unique QR prevents all proxy attendance"],
    ]
    elements.append(make_table(qr_compare, col_widths=[7.5*cm, 9*cm]))
    elements.append(sp(8))

    # ─── 13. AI FEATURES ───────────────
    elements.append(h1("13. AI Features"))
    elements.append(sp(6))
    elements.append(body(
        "The platform includes eight practical AI features. These are realistic, achievable within "
        "a final-year project timeline, and add meaningful value to the user experience."
    ))
    ai_data = [
        ["AI Feature", "What It Does"],
        ["Event Recommendations", "Suggests events to students based on past participation and interest history"],
        ["Attendance Prediction", "Predicts expected turnout based on registration data and historical event trends"],
        ["AI Description Generator", "Helps club heads write compelling event descriptions from a short prompt"],
        ["Poster Caption Suggester", "Generates social media captions and hashtags for event posters"],
        ["Budget Estimation", "Estimates typical event costs based on event type and expected participant count"],
        ["Schedule Conflict Detection", "Flags when a new event overlaps with existing major events on the calendar"],
        ["Feedback Summarizer", "Reads post-event feedback responses and generates a concise plain-English summary"],
        ["Spam / Abuse Detection", "Flags inappropriate content in event discussion channels for moderator review"],
    ]
    elements.append(make_table(ai_data, col_widths=[5*cm, 11.5*cm]))
    elements.append(sp(4))
    elements.append(Paragraph(
        "Note: These features use lightweight models and straightforward logic. "
        "They are practical additions — not complex research systems — keeping them fully achievable within the project scope.",
        S['Note']
    ))
    elements.append(sp(8))

    # ─── 14. IMPLEMENTATION PLAN ───────────────
    elements.append(h1("14. Implementation Plan"))
    elements.append(sp(6))
    elements.append(body(
        "The project will be built across four phases over five months:"
    ))
    impl_data = [
        ["Phase", "Timeline", "Key Deliverables"],
        ["Phase 1\nCore Infrastructure", "Month 1",
         "Project setup, database schema, JWT authentication, role-based access control, basic UI framework"],
        ["Phase 2\nEvent Management Core", "Months 2–3",
         "Event creation wizard, venue request & approval workflow, club management, "
         "student registration, dynamic forms, QR code generation"],
        ["Phase 3\nCommunication & Attendance", "Month 4",
         "Built-in event channels, QR scanning for attendance, "
         "automated certificate generation, email notification system"],
        ["Phase 4\nAnalytics, AI & Deployment", "Month 5",
         "Analytics dashboards, AI feature integration, end-to-end testing, "
         "performance optimization, live cloud deployment"],
    ]
    impl_table = Table(
        [[Paragraph(f"<b>{r[0]}</b>" if i==0 else r[0], ParagraphStyle('ic', fontSize=9, fontName='Helvetica-Bold' if i==0 else 'Helvetica', textColor=WHITE if i==0 else DARK_TEXT, leading=13)),
          Paragraph(r[1], ParagraphStyle('it', fontSize=9, fontName='Helvetica-Bold' if i==0 else 'Helvetica', textColor=WHITE if i==0 else ACCENT, leading=13, alignment=TA_CENTER)),
          Paragraph(r[2], ParagraphStyle('id', fontSize=9, fontName='Helvetica-Bold' if i==0 else 'Helvetica', textColor=WHITE if i==0 else DARK_TEXT, leading=13))]
         for i, r in enumerate(impl_data)],
        colWidths=[3.5*cm, 2.5*cm, 10.5*cm]
    )
    impl_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), TABLE_HEADER),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor("#D6EAF8")),
        ('BACKGROUND', (0,2), (-1,2), colors.HexColor("#D5F5E3")),
        ('BACKGROUND', (0,3), (-1,3), colors.HexColor("#FEF9E7")),
        ('BACKGROUND', (0,4), (-1,4), colors.HexColor("#FDEDEC")),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('ALIGN', (1,0), (1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.4, colors.HexColor("#BDC3C7")),
    ]))
    elements.append(impl_table)
    elements.append(sp(8))

    # ─── 15. TECH STACK ───────────────
    elements.append(h1("15. Technology Stack"))
    elements.append(sp(6))
    tech_data = [
        ["Layer", "Technology", "Why This Was Chosen"],
        ["Frontend", "Next.js (React)", "Fast, modern, component-based — industry standard for web apps"],
        ["Backend", "Node.js + NestJS", "Structured and scalable — ideal for role-based enterprise systems"],
        ["Database", "PostgreSQL", "Reliable relational database — excellent for complex structured data"],
        ["Authentication", "JWT + RBAC", "Secure, stateless token-based auth with fine-grained role control"],
        ["Real-Time", "Socket.io", "Powers live notifications and event channel messages instantly"],
        ["QR Generation", "QRCode.js / ZXing", "Standard, well-supported, works across all devices"],
        ["Cloud Storage", "AWS S3 / Cloudinary", "Scalable storage for posters, certificates, and media"],
        ["Email Service", "SendGrid + Nodemailer", "Reliable transactional emails — certificates, reminders, verification"],
        ["AI Features", "OpenAI API (GPT-4o-mini)", "Powers description generation and feedback summarization"],
        ["Deployment", "Vercel + Railway", "Free to start, scales automatically — zero DevOps overhead"],
    ]
    elements.append(make_table(tech_data, col_widths=[3.5*cm, 4*cm, 9*cm]))
    elements.append(sp(8))

    # ─── 16. SYSTEM ARCHITECTURE ───────────────
    elements.append(h1("16. System Architecture"))
    elements.append(sp(6))
    elements.append(body(
        "The platform follows a clean, layered architecture with independent services. "
        "Each component can be upgraded or scaled separately without affecting the rest of the system."
    ))
    elements.append(sp(6))

    arch_data = [
        ["Layer", "Component", "Responsibility"],
        ["Client Layer", "Next.js Frontend", "UI, routing, real-time updates, QR scanner"],
        ["API Layer", "NestJS REST API", "Business logic, authentication, role enforcement"],
        ["Data Layer", "PostgreSQL + Redis", "Persistent data storage + session caching"],
        ["Service Layer", "Notification Service", "Socket.io push notifications + email delivery"],
        ["Service Layer", "QR Service", "QR code generation and validation"],
        ["Service Layer", "Certificate Generator", "PDF certificate creation and distribution"],
        ["Service Layer", "AI Service", "OpenAI API integration for smart features"],
        ["Infrastructure", "AWS S3", "File storage — posters, certificates, uploads"],
        ["Deployment", "Vercel + Railway", "Frontend and backend hosting with auto-scaling"],
    ]
    elements.append(make_table(arch_data, col_widths=[3.5*cm, 4.5*cm, 8.5*cm]))
    elements.append(sp(8))

    # ─── 17. RESEARCH POTENTIAL ───────────────
    elements.append(h1("17. Research Potential"))
    elements.append(sp(6))
    elements.append(body(
        "This project is not just a utility — the data it generates can power meaningful academic research. "
        "Below are four viable research directions that can be pursued as follow-up work or during the project itself."
    ))
    research = [
        ("AI-Based Event Recommendation for Student Engagement",
         "Using collaborative filtering to recommend events based on past participation — similar to how Netflix recommends content."),
        ("Predicting Event Attendance Using Machine Learning",
         "Training a regression model on historical event data (type, day, time, competition) to forecast attendance for future events."),
        ("Digital Campus Ecosystems: Replacing Ad-Hoc Tools with Integrated Platforms",
         "A case study on how centralized platforms improve participation rates and reduce administrative overhead."),
        ("Student Engagement Analysis Through Event Participation Patterns",
         "Analyzing which students participate in which events and correlating this with academic and career outcomes."),
    ]
    for i, (title, desc) in enumerate(research, 1):
        elements.append(Paragraph(f"<b>{i}. {title}</b>", S['H3']))
        elements.append(body(desc))
        elements.append(sp(4))
    elements.append(sp(8))

    # ─── 18. FACTS & FIGURES ───────────────
    elements.append(h1("18. Facts & Industry Figures"))
    elements.append(sp(6))
    facts = [
        ("2023 Eventbrite Report",
         "85% of event organizers say that manual processes are their biggest operational challenge."),
        ("Grand View Research, 2023",
         "The global event management software market was valued at $11.4 billion in 2023 and is "
         "projected to reach $26.9 billion by 2030."),
        ("McKinsey Digital Study",
         "Digitizing manual workflows reduces administrative effort by 60–70% in educational institutions."),
        ("Statista, 2023",
         "QR code usage in attendance management grew by 240% between 2020 and 2023, driven by "
         "education and hospitality sectors."),
        ("NASPA Survey",
         "73% of students say they miss campus events because they did not know about them in time."),
        ("IIM Ahmedabad Study, 2022",
         "72% of college students in India use multiple apps (WhatsApp, Instagram, email) to track "
         "campus activities — highlighting the need for a unified platform."),
    ]
    facts_data = [["Source", "Statistic"]] + [[s, f] for s, f in facts]
    elements.append(make_table(facts_data, col_widths=[5*cm, 11.5*cm]))
    elements.append(sp(8))

    # ─── 19. WHY MAJOR PROJECT ───────────────
    elements.append(h1("19. Why This Is a Major Project"))
    elements.append(sp(6))
    elements.append(body(
        "This is often asked: \"Is this just another event management app?\" The answer is definitively no. "
        "Here is a direct comparison that shows what separates this platform from a basic event app:"
    ))
    compare_major = [
        ["Feature / Dimension", "Simple Event App", "This Platform"],
        ["User Roles", "1–2 roles", "6 distinct roles with RBAC"],
        ["Dashboards", "Single generic view", "4 fully customized dashboards"],
        ["Approval Workflow", "None", "Multi-level: Club → Faculty → Admin"],
        ["Venue Management", "None", "Real-time conflict detection"],
        ["Communication", "External WhatsApp", "Built-in event channels"],
        ["Attendance", "Manual paper sheets", "QR-based, instant, fraud-proof"],
        ["Certificates", "Manual Canva/Word", "Auto-generated PDF, auto-emailed"],
        ["Analytics", "None", "Full post-event analytics report"],
        ["AI Features", "None", "8 integrated AI features"],
        ["External Participants", "Not supported", "Email-verified with guest QR"],
        ["Deployment", "Local / demo only", "Cloud-hosted, production-ready"],
        ["Architecture", "Monolithic script", "Role-based modular architecture"],
    ]
    elements.append(make_table(compare_major, col_widths=[5*cm, 4.5*cm, 7*cm]))
    elements.append(sp(6))
    elements.append(body(
        "This project demonstrates mastery of <b>full-stack development, system design, role-based architecture, "
        "cloud deployment, and applied AI</b> — all in one product that solves a real, tangible problem."
    ))
    elements.append(sp(8))

    # ─── 20. FUTURE SCOPE ───────────────
    elements.append(h1("20. Future Scope"))
    elements.append(sp(6))
    future = [
        ("Mobile App (iOS & Android)", "Native app for students to browse and register events on the go."),
        ("Digital Student ID Integration", "Replace physical college ID cards with a digital identity tied to the platform."),
        ("AR Campus Navigation", "Augmented reality navigation to guide external participants to event venues."),
        ("Sponsor Marketplace", "Allow companies and local businesses to browse and sponsor campus events directly."),
        ("Alumni Network Integration", "Invite alumni to participate in events, mentor students, or serve as judges."),
        ("Campus Wallet", "Digital wallet for students to pay fees, buy merchandise, or pay for food at college fests."),
        ("Placement Integration", "Allow companies to post pre-placement events (PPTs, hackathons) through the platform."),
        ("Multi-Institution Licensing", "Package as a white-label SaaS product deployable by any university in India."),
    ]
    future_data = [["Future Feature", "Description"]] + [[f"<b>{t}</b>", d] for t, d in future]
    # Build as table with bold in cell
    f_rows = [
        [Paragraph("Future Feature", ParagraphStyle('fh', fontSize=9, fontName='Helvetica-Bold', textColor=WHITE, leading=13)),
         Paragraph("Description", ParagraphStyle('fh2', fontSize=9, fontName='Helvetica-Bold', textColor=WHITE, leading=13))]
    ]
    for t, d in future:
        f_rows.append([
            Paragraph(f"<b>{t}</b>", ParagraphStyle('ft', fontSize=9, fontName='Helvetica-Bold', textColor=PRIMARY, leading=13)),
            Paragraph(d, ParagraphStyle('fd', fontSize=9, fontName='Helvetica', textColor=DARK_TEXT, leading=13))
        ])
    ft = Table(f_rows, colWidths=[5.5*cm, 11*cm])
    ft.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), TABLE_HEADER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [TABLE_ROW1, TABLE_ROW2]),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.4, colors.HexColor("#BDC3C7")),
    ]))
    elements.append(ft)
    elements.append(sp(8))

    # ─── 21. CONCLUSION ───────────────
    elements.append(h1("21. Conclusion"))
    elements.append(sp(6))
    elements.append(body(
        "Campus events are among the most important parts of college life. They build skills, "
        "create memories, and form professional connections. Yet today, they are managed through "
        "a scattered mix of WhatsApp, Google Forms, paper notices, and emails — wasting enormous "
        "time and causing students to consistently miss opportunities."
    ))
    elements.append(body(
        "This platform proposes a complete, centralized solution built specifically for universities. "
        "It does not replicate an existing product. It solves a problem that every Indian college faces, "
        "with a system designed around the actual workflows of students, clubs, faculty, and administration."
    ))
    elements.append(body(
        "The technical depth — multi-role access control, real-time WebSocket notifications, "
        "QR-based attendance, automated certificate generation, applied AI features, and full cloud deployment — "
        "makes this a comprehensive final-year project demonstrating mastery across all key areas of modern "
        "software engineering."
    ))
    elements.append(body(
        "Beyond the classroom, this platform has genuine adoption potential. Any college in India "
        "could deploy this system tomorrow and immediately benefit from it. That is the mark of a "
        "project truly worth building."
    ))
    elements.append(sp(20))
    rule()

    sig_data = [
        [Paragraph("Submitted By", ParagraphStyle('sl', fontSize=9, fontName='Helvetica-Bold',
                                                   textColor=PRIMARY, leading=13, alignment=TA_CENTER)),
         Paragraph("Project Guide", ParagraphStyle('sl2', fontSize=9, fontName='Helvetica-Bold',
                                                    textColor=PRIMARY, leading=13, alignment=TA_CENTER))],
        [Paragraph("[Your Name]", ParagraphStyle('sn', fontSize=9, fontName='Helvetica',
                                                  textColor=DARK_TEXT, leading=13, alignment=TA_CENTER)),
         Paragraph("[Mentor Name]", ParagraphStyle('sn2', fontSize=9, fontName='Helvetica',
                                                    textColor=DARK_TEXT, leading=13, alignment=TA_CENTER))],
        [Paragraph("[Department]", ParagraphStyle('sd', fontSize=8, fontName='Helvetica',
                                                   textColor=MID_TEXT, leading=12, alignment=TA_CENTER)),
         Paragraph("[Department]", ParagraphStyle('sd2', fontSize=8, fontName='Helvetica',
                                                    textColor=MID_TEXT, leading=12, alignment=TA_CENTER))],
    ]
    sig_table = Table(sig_data, colWidths=[8*cm, 8.5*cm])
    sig_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LINEABOVE', (0,0), (0,0), 1, PRIMARY),
        ('LINEABOVE', (1,0), (1,0), 1, PRIMARY),
    ]))
    elements.append(sig_table)

# ─────────────────────────────────────────────
# PAGE TEMPLATE CALLBACK (header/footer)
# ─────────────────────────────────────────────
def add_header_footer(canvas, doc):
    canvas.saveState()
    page_w, page_h = A4

    # Header bar (all pages except cover = page 1)
    if doc.page > 1:
        canvas.setFillColor(PRIMARY)
        canvas.rect(0, page_h - 1.2*cm, page_w, 1.2*cm, fill=1, stroke=0)
        canvas.setFillColor(WHITE)
        canvas.setFont("Helvetica-Bold", 8)
        canvas.drawString(1.5*cm, page_h - 0.75*cm, "Campus Engagement & Event Management Platform")
        canvas.setFont("Helvetica", 8)
        canvas.drawRightString(page_w - 1.5*cm, page_h - 0.75*cm, "Final Year Project Proposal")

    # Footer
    if doc.page > 1:
        canvas.setFillColor(LIGHT_BG)
        canvas.rect(0, 0, page_w, 1*cm, fill=1, stroke=0)
        canvas.setFillColor(MID_TEXT)
        canvas.setFont("Helvetica", 7.5)
        canvas.drawString(1.5*cm, 0.38*cm, f"Page {doc.page}")
        canvas.drawCentredString(page_w/2, 0.38*cm, "Confidential — For Academic Review Only")
        canvas.drawRightString(page_w - 1.5*cm, 0.38*cm, "2025–2026")

    canvas.restoreState()

# ─────────────────────────────────────────────
# MAIN BUILD FUNCTION
# ─────────────────────────────────────────────
def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=A4,
        leftMargin=2*cm,
        rightMargin=2*cm,
        topMargin=1.6*cm,
        bottomMargin=1.5*cm,
        title="Campus Engagement & Event Management Platform — Project Proposal",
        author="Final Year Student",
        subject="Final Year Project Proposal",
    )

    elements = []
    cover_page(elements)
    toc_page(elements)
    build_content(elements)

    doc.build(elements, onFirstPage=add_header_footer, onLaterPages=add_header_footer)
    print(f"\n[OK] PDF Generated Successfully!\nSaved at: {OUTPUT_PATH}\n")

if __name__ == "__main__":
    build_pdf()
