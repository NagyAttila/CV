from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Define the PDF file path
pdf_path = "./Attila_Nagy_Lafayette_Cover_Letter.pdf"

# Define styles
styles = getSampleStyleSheet()
style = styles["Normal"]
style.fontName = "Helvetica"
style.fontSize = 11
style.leading = 14

# Define the content starting from "To the Hiring Manager"
content = """
Dear Lafayette AB,

I am writing to express my interest in the position of Hårdvarunära mjukvaruutvecklare at Lafayette AB. With a background spanning embedded systems, automotive software, and telecommunications, I have extensive experience developing and testing software that operates close to hardware — from GNSS positioning and sensor fusion to network protocol stacks and real-time embedded systems.

Over the past few years, I have worked as a consultant at <b>Volvo Cars</b>, focusing on <b>GNSS and dead-reckoning</b> systems in the infotainment platform. This role requires both high-level algorithmic design and low-level debugging on multiple ECUs, combining C++ development, hardware validation, and cross-team collaboration. I have also contributed to legacy product maintenance, ensuring software reliability across different vehicle variants and markets.

Prior to that, I worked at Ericsson on PacketCore systems, developing and functionally testing telecom software using C++ and TTCN, and at RumbleStrip, where I built a Bayesian regression model running on <b>STM32</b> microcontroller to optimize truck aerodynamics. These projects strengthened my skills in embedded programming, signal processing, and system testing under real-world constraints. My earlier experience at Volvo Cars Active Safety further deepened my understanding of sensor fusion, data analysis, and automotive system integration.

Across all these positions, I’ve consistently worked at the interface between hardware and software — debugging signal timing, optimizing algorithms for embedded processors, and ensuring systems perform reliably under real-time conditions. I’m comfortable working in <b>C, C++, Python</b>, and Matlab environments, and I use tools like <b>Git, Gerrit, and GDB</b> daily.

What motivates me most is contributing to technically challenging products that bridge the digital and physical worlds — exactly the kind of work Lafayette AB is known for. I value well-structured software, rigorous testing, and open collaboration with hardware engineers to deliver robust, maintainable solutions.

I would be very excited to bring my experience in embedded development, system testing, and hardware-software integration to Lafayette AB, and I’m eager to learn more about your current projects.

Thank you for considering my application. I look forward to the possibility of discussing how my background can contribute to your team.

Kind regards,<br/>
Attila Nagy
"""

# Build the PDF document
doc = SimpleDocTemplate(pdf_path, pagesize=A4, topMargin=72, bottomMargin=72, leftMargin=72, rightMargin=72)
story = []

for paragraph in content.strip().split("\n\n"):
    story.append(Paragraph(paragraph.strip(), style))
    story.append(Spacer(1, 12))

doc.build(story)

pdf_path
