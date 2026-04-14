---
title: "Emerging Digital Technologies — Session 12: Hands-On RPA with Microsoft Power Apps and UiPath"
category: references
tags: ["#src/course", "#dba/coursework", "#emerging-digital-technologies"]
sources:
  - "_raw/dba-course/Course_03_Emerging_Digital_Technologies/02_Recordings_and_PPTs/Session_12/transcript.txt"
created: 2026-04-13
updated: 2026-04-13
summary: "A fully practical session in which students built a live data-connected app in Microsoft Power Apps and automated email dispatch through UiPath Studio, experiencing both platforms' integration capabilities and limitations firsthand."
---

# Emerging Digital Technologies — Session 12: Hands-On RPA with Microsoft Power Apps and UiPath

**Instructor**: [[dr-sumitra-padman|Dr. Sumitra Padman]] (referred to as "Dr. V" and "Prof" in the session)
**Date**: Session 12 (exact date not stated in transcript; recorded session available at https://www.youtube.com/watch?v=KHqndz5ElF0)
**Course**: Emerging Digital Technologies (Course 03)

Session 12 is an almost entirely practical, hands-on session. After a brief recap of the previous lecture — which covered the introduction, features, limitations, and governance of Robotic Process Automation (RPA), the taxonomy of attended vs. unattended robots, and the three-tier automation maturity model (basic scripting → intermediate RPA → intelligent process automation) — the instructor pivots immediately to live tool demonstrations with students working along in real time.

The first major demonstration uses Microsoft Power Apps, a low-code/no-code platform from Microsoft's Power Platform suite. Students create a blank canvas app from scratch, connect it to a shared Google Sheet containing a course schedule, and build a vertical gallery to display the data alongside an editable form. The exercise surfaces a range of real-world friction points: rate-limit errors from Google's API when multiple students connect to the same sheet simultaneously, browser compatibility issues (Power Apps performs poorly on Safari; students on M-series Macs face UiPath installation barriers), and the distinction between editing a data *source* vs. editing an individual *item* — a conceptual misunderstanding that caused the edit form to remain disconnected from the gallery for many students.

The second major demonstration uses UiPath Studio (desktop version) to automate email dispatch via an SMTP connection. Students create a new RPA workflow process, add a Send SMTP Email activity, configure a Gmail SMTP connection (server: smtp.gmail.com, port: 587), generate a Gmail app password rather than using their master Gmail password, and trigger the workflow to send a test email. The session closes with the instructor noting that the intended third activity — using UiPath to bulk-send personalized emails by reading recipient data from an Excel spreadsheet — could not be completed due to time constraints, and that a follow-up practical session has been requested.

## Key Concepts

- **Automation Maturity Tiers** — The session opens with a recap of the three-tier model introduced in the previous class. *Basic automation* uses simple scripts, macros, and remote-desktop scripting (e.g., auto-formatting Excel reports). *Intermediate automation (RPA)* handles structured, repetitive tasks such as chatbots answering HR FAQs. *Intelligent Process Automation (IPA)* adds cognitive capabilities — OCR, NLP, fraud detection from scanned bills — where AI is embedded into the automation pipeline. This hierarchy frames the rationale for learning both Power Apps and UiPath: they occupy the intermediate tier and serve as on-ramps to the intelligent tier.

- **Low-Code / No-Code Application Development (Power Apps)** — Microsoft Power Apps is positioned as a no-installation, browser-based platform for building business applications without traditional coding. Students access it through their GGU (Golden Gate University) institutional accounts. The platform supports three layout modes — phone, tablet, and responsive — and provides a visual canvas editor where components (galleries, forms, buttons) are inserted from a toolbar and connected to data sources via formula expressions. The instructor frames it as an alternative to UiPath and Automation Anywhere for automation tasks, with added value in its tight integration with the broader Microsoft Power Platform (including Power Automate and Copilot Studio).

- **Canvas App Architecture: Gallery + Edit Form Pattern** — The core design pattern demonstrated is the two-panel CRUD interface: a *vertical gallery* on the left to browse records and an *edit form* on the right to modify the selected record. The gallery is bound to a data source (the Google Sheet). The form's `Item` property must be set to `Gallery1.Selected` in the formula bar so that clicking a row in the gallery populates the form with that specific row's data. Confusion between setting `DataSource` and `Item` in the form's mode dropdown was the most common student error of the session.

- **Data Connectivity and API Rate Limits** — Connecting Power Apps to Google Sheets requires OAuth authorization through a Google account. The instructor explains that load time is proportional to the number of sheets in the user's Google Drive because the API enumerates all available sheets before returning results. When twenty-plus students tried to connect to the same shared Google Sheet simultaneously, they encountered "service rate limit has been reached" and "too many requests sent to Google API" errors — a practical lesson in the real-world constraints of SaaS API quotas. The workaround students used was to copy the sheet to their personal Google Drive and rename it to make it unique.

- **Formula Bar and Power Fx Expressions** — Power Apps uses Power Fx, a low-code expression language. During the session the most important expression is `Gallery1.Selected`, entered in the formula bar while the edit form is selected, to bind the form to the gallery's selected row. The instructor also explains the `SubmitForm(Form1)` function, entered in the button's `OnSelect` property under the Advanced tab, to write changes back to the data source. These expressions are case-sensitive and require the exact form/gallery name (which can differ from "Form1" or "Gallery1" if components were created in a different order).

- **Bidirectional Sync Between App and Data Source** — Once the app and the Google Sheet are connected, changes made in the Power Apps form are pushed to the sheet when the Save button is pressed, and changes made directly in the sheet are visible in the app after a manual refresh (three dots → Refresh on the data source in the left panel). The instructor acknowledges that automatic background sync is a known limitation of the current Power Apps–Google Sheets connector: the data is updated internally, but the gallery display does not auto-refresh without a manual trigger.

- **Collaboration and Access Control** — The intent of the shared-sheet exercise is to illustrate collaborative data management: multiple users connected to the same data source can all read and update records, simulating a shared operations dashboard. The instructor notes that this openness is also a governance risk — without additional logic, any user can overwrite any record. Power Apps supports addressing this through conditional logic (e.g., a conditional insert requiring a password or role check), which the instructor mentions as a possible extension but does not demonstrate due to time.

- **UiPath Studio as an RPA IDE** — UiPath Studio (desktop version) is a graphical workflow designer where automation sequences are built by adding *activities* from a panel, configuring their properties, and connecting them into a flow. The session focuses on one activity: **Send SMTP Email**. The instructor explains that Studio is just an IDE; the actual capability to send email comes from the activity *package*, which must be downloaded from UiPath's package manager the first time it is used. On Mac (especially M-series chips), the .MSI installer does not run natively; Mac users must use UiPath's web Studio or set up a Windows virtualization environment.

- **SMTP Email Automation with UiPath** — The Send SMTP Email activity requires four configuration values: `Server` (smtp.gmail.com), `Port` (587), `Email` (the sender's Gmail address), and `Password` (a Gmail *app password*, not the account password). App passwords are 16-character tokens generated in the Google account security settings under "App passwords." This indirection is necessary because Google's SMTP service requires an app-specific credential when two-factor authentication is enabled. Once connected, the activity's `To`, `Subject`, and `Body` fields accept string literals (wrapped in double quotes) or UiPath variables. The workflow is run by clicking the Debug / Play button, which executes the sequence and delivers the email.

- **Bulk Email Automation via Excel Integration** — The session ends with the instructor describing (but not completing) the next planned activity: connecting the Send SMTP Email activity to an Excel workbook that contains columns for recipient address, subject, and body text. UiPath would iterate through each row with a ForEach loop, sending a personalized email to each recipient. This pattern illustrates the leap from a manual task (sending one email) to a scalable automation (sending hundreds of differentiated emails), which is the core value proposition of RPA. The Excel file must contain a properly formatted Table object (not just raw rows) for UiPath to read it correctly.

- **Variables and Concatenation in UiPath** — A student asked how to personalize the email body (e.g., "Dear [Name]") for each recipient. The instructor demonstrates creating a variable in UiPath's Data Manager panel and using it in the `Body` field via the Use Variable picker. String concatenation in the body field is done by connecting a quoted string to a variable with the `&` operator, for example: `"Hello " & recipientName`. This concept — that body text is a string expression, not a free-text field — is the conceptual bridge between static email content and data-driven, personalized messaging.

- **Browser and Platform Compatibility** — A recurring theme throughout the session is that the tools behave differently across environments. Power Apps does not support Safari; Microsoft Edge or Chrome is required. UiPath's desktop installer is Windows-only; Mac users must either use the web Studio (which lacks some desktop features) or run a Windows virtual machine. These constraints highlight a practical challenge for organizations deploying automation toolchains in heterogeneous IT environments.

## Technologies / Frameworks Discussed

| Technology | Type | Key Point |
|---|---|---|
| Microsoft Power Apps | Low-code application builder | Browser-based canvas editor; connects to 200+ data sources including Google Sheets and SharePoint; part of Microsoft Power Platform |
| Microsoft Power Automate | Workflow automation (integration) | Mentioned as a natural companion to Power Apps for automating backend flows; not demonstrated in this session |
| Microsoft Copilot Studio | AI-enhanced automation | Instructor mentions potential to integrate Copilot into Power Apps apps; not demonstrated |
| Power Fx | Formula language | Expression language behind Power Apps canvas formulas; used for `Gallery1.Selected` and `SubmitForm(Form1)` |
| Google Sheets API | Cloud data source | Used as the live backend for the Power Apps canvas app; subject to API rate limits with concurrent OAuth connections |
| UiPath Studio (Desktop) | RPA IDE | Graphical workflow designer; activity-based; packages downloaded on demand; Windows only for full desktop install |
| UiPath Studio Web | RPA IDE (browser) | Cloud-based alternative; lacks some desktop features; usable on Mac with limitations |
| UiPath Cloud | Orchestration platform | Required for initial sign-in/organization setup; organization name can be any arbitrary string during first-time setup |
| Send SMTP Email (UiPath Activity) | Email automation activity | Configured with smtp.gmail.com:587; requires Gmail app password; accepts To, Subject, Body as string variables |
| Gmail App Password | Authentication token | 16-character app-specific password generated in Google Account settings; required when SMTP is used with 2FA-enabled accounts |

## Important Examples and Case Studies

**Course Schedule App in Power Apps** — The instructor shares a Google Sheet containing a university course schedule (columns: serial number, subject, faculty name, time, day, date, mode — online/offline). Students connect their Power Apps canvas to this sheet, display the schedule in a vertical gallery, and build an edit form linked to the gallery via `Gallery1.Selected`. After adding a "Save Changes" button bound to `SubmitForm(Form1)`, students can change a row's day field (e.g., from "TUD" to "Wednesday") in the app and see the change reflected in the Google Sheet — and vice versa. The shared-sheet setup means all students are writing to the same data source, visibly demonstrating collaborative real-time editing. The instructor uses this to discuss both the power and the governance risk of open multi-user write access.

**UiPath Email Automation Test** — Students configure a Send SMTP Email activity to send a self-addressed test email from their personal Gmail account. The exercise requires generating a Gmail app password, which several students encounter for the first time. Common errors during this exercise include: using the Gmail master password instead of the app password (resulting in "username and password" authentication errors), failing to wrap the `To`, `Subject`, and `Body` values in double quotes (producing "invalid character in mail header" errors), and gallery/form naming mismatches (e.g., `Gallery2` instead of `Gallery1`). Each error category is resolved live during the session through screen-sharing troubleshooting. At least two students successfully send and receive test emails by the end of the session.

**Bulk Personalized Email via Excel + UiPath (Described, Not Completed)** — The instructor describes the architecture of the intended Excel-driven email activity: an Excel workbook with columns for recipient email, subject line, and body text; a UiPath ForEach loop iterating over rows; and the Send SMTP Email activity receiving each row's values as variables. This pattern generalizes to any scenario requiring high-volume, personalized outbound communication — marketing campaigns, HR notifications, invoice dispatch — and is the canonical RPA use case for SMTP automation. The step-by-step instructions were uploaded to the instructor's Google Drive folder and shared with the class at the end of the session.

**Power Apps vs. UiPath as Automation Alternatives** — The instructor explicitly positions Power Apps not as a replacement for UiPath but as an alternative automation pathway. Both platforms can automate repetitive tasks; Power Apps excels at building user-facing interfaces backed by live data, while UiPath excels at back-end, headless process execution. The session illustrates that choosing between them depends on whether the task requires human interaction (Power Apps) or can run unattended (UiPath).

## Related

- [[course-03-overview-emerging-digital-technologies|Course 03 Overview]]
- [[robotic-process-automation|Robotic Process Automation (RPA)]]
- [[intelligent-process-automation|Intelligent Process Automation (IPA)]]
- [[attended-vs-unattended-bots|Attended vs. Unattended Robots]]
- [[microsoft-power-platform|Microsoft Power Platform]]
- [[power-automate|Power Automate]]
- [[uipath|UiPath]]
- [[low-code-no-code|Low-Code / No-Code Development]]
- [[smtp-email-automation|SMTP Email Automation]]
- [[automation-governance|Automation Governance]]
- [[rpa-use-cases|RPA Use Cases in Business]]
