import turtle
import random
 
# Create screen
screen = turtle.Screen()
screen.bgcolor("#07111F")
screen.setup(width=1000, height=700)
screen.title("The Missing Diamond")
 
# Create pen
pen = turtle.Turtle()
pen.color("#D4AF37")
pen.hideturtle()
pen.penup()
pen.speed(0)
 
current_screen = "menu"
 
clues_found = []
 
security_found = False
fingerprints_found = False
keycard_found = False
financial_found = False
witness_found = False
 
suspects = [
    "Emma",
    "David",
    "Sophie",
    "Michael"
]
 
full_names = {
    "Emma": "Emma Brooks",
    "David": "David Turner",
    "Sophie": "Sophie Reed",
    "Michael": "Michael Lee"
}
 
culprit = random.choice(suspects)
 
message_pen = turtle.Turtle()
message_pen.color("#D4AF37")
message_pen.hideturtle()
message_pen.penup()
# -----------------
# MENU SCREEN
# -----------------
def draw_button(x, y, width, height, text):
 
    # SHADOW
 
    pen.fillcolor("#C9A227")
    pen.pencolor("#C9A227")
 
    pen.penup()
    pen.goto(x + 6, y - 6)
    pen.pendown()
 
    pen.begin_fill()
 
    for _ in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)
 
    pen.end_fill()
 
    # BUTTON
 
    pen.fillcolor("#12355B")
    pen.pencolor("#D4AF37")
 
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
 
    pen.begin_fill()
 
    for _ in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)
 
    pen.end_fill()
 
    pen.penup()
 
    # TEXT
 
    pen.goto(x + width/2, y - 37)
 
    pen.write(
        text,
        align="center",
        font=("Arial", 14, "bold")
    )
 
def draw_portrait_box(x, y):
 
    pen.goto(x, y)
    pen.pendown()
 
    for _ in range(2):
        pen.forward(150)
        pen.right(90)
        pen.forward(180)
        pen.right(90)
 
    pen.penup()
 
def draw_face(x, y, face_colour, hair_colour):
 
    # Head
 
    pen.goto(x, y)
 
    pen.fillcolor(face_colour)
 
    pen.begin_fill()
 
    pen.pendown()
 
    pen.circle(40)
 
    pen.end_fill()
 
    pen.penup()
 
    # Left eye
 
    pen.goto(x - 15, y + 55)
 
    pen.dot(8, "black")
 
    # Right eye
 
    pen.goto(x + 15, y + 55)
 
    pen.dot(8, "black")
 
    # Mouth
 
    pen.goto(x - 15, y + 25)
 
    pen.pendown()
 
    pen.goto(x + 15, y + 25)
 
    pen.penup()
 
    # Hair
    pen.fillcolor(hair_colour)
   
    pen.goto(x - 40, y + 80)
   
    pen.begin_fill()
   
    pen.goto(x + 40, y + 80)
    pen.goto(x + 40, y + 65)
    pen.goto(x - 40, y + 65)
    pen.goto(x - 40, y + 80)
   
    pen.end_fill()
 
    pen.penup()
 
def show_menu():
 
    global current_screen
    current_screen = "menu"
 
    pen.clear()
    draw_diamond(0, 390)
    pen.goto(0, 170)
   
    pen.write(
        "THE MISSING DIAMOND",
        align="center",
        font=("Arial", 24, "bold")
    )
 
    pen.goto(0, 75)
    pen.write(
        "A Detective Mystery Game",
        align="center",
        font=("Arial", 14, "italic")
    )
   
    draw_button(
        -150,
        50,
        300,
        60,
        "START GAME"
    )
 
 
# -----------------
# HUB SCREEN
# -----------------
def show_hub():
 
    global current_screen
    current_screen = "hub"
 
    pen.clear()
 
    pen.goto(0, 250)
 
    pen.write(
        "INVESTIGATION HUB",
        align="center",
        font=("Arial", 24, "bold")
    )
 
    draw_button(
        -350,
        100,
        250,
        60,
        "SUSPECTS"
    )
 
    draw_button(
        100,
        100,
        250,
        60,
        "EVIDENCE"
    )
 
    draw_button(
        -350,
        -20,
        250,
        60,
        "CRIME SCENE"
    )
 
    draw_button(
        100,
        -20,
        250,
        60,
        "NOTEBOOK"
    )
 
    draw_button(
        -125,
        -140,
        250,
        60,
        "ACCUSE"
    )
 
def show_suspects():
 
    global current_screen
    current_screen = "suspects"
 
    pen.clear()
 
    pen.goto(0, 250)
 
    pen.write(
        "SUSPECTS",
        align="center",
        font=("Arial", 24, "bold")
    )
 
    draw_button(
        -400,
        200,
        200,
        60,
        "EMMA"
    )
 
    draw_button(
        -400,
        100,
        200,
        60,
        "DAVID"
    )
 
    draw_button(
        -400,
        0,
        200,
        60,
        "SOPHIE"
    )
 
    draw_button(
        -400,
        -100,
        200,
        60,
        "MICHAEL"
    )
 
    draw_button(
        -150,
        -220,
        300,
        60,
        "BACK"
    )
 
def show_emma():
 
    global current_screen
    current_screen = "emma"
 
    pen.clear()
 
    pen.goto(0, 250)
 
    pen.write(
        "EMMA BROOKS",
        align="center",
        font=("Arial", 24, "bold")
    )
 
    pen.goto(-250, 100)
   
    pen.write(
        "Role: Museum Curator\n"
        "Experience: 12 Years\n"
        "Access Level: High",
        font=("Arial", 14, "normal")
    )
 
    if culprit == "Emma":
        statement = (
             "\"I was preparing exhibits "
             "alone in my office.\""\
        )
       
    else:
        statement = (
            "\"I was preparing exhibits "
            "with two museum volunteers.\""
        )
       
    pen.goto(-250, 80)
   
    pen.write(
        statement,
        font=("Arial", 16, "normal")
    )
 
    draw_portrait_box(-100, 50)
 
    draw_face(
        -25,
        -70,
        "#F4D7B5",
        "#8B5A2B"
    )
 
    pen.fillcolor("#8B5A2B")
    pen.goto(-60, 20)
   
    pen.begin_fill()
   
    pen.goto(10, 20)
    pen.goto(10, -20)
    pen.goto(-60, -20)
    pen.goto(-60, 20)
   
    pen.end_fill()
 
    draw_face(
        -25,
        -70,
        "#F4D7B5",
        "#8B5A2B"
    )
 
    # Badge
    pen.goto(-25, -120)
    pen.write(
        "ID",
        align="center",
        font=("Arial", 8, "bold")
    )
   
    draw_button(
        -150,
        -220,
        300,
        60,
        "BACK"
    )
 
def show_david():
 
    global current_screen
    current_screen = "david"
 
    pen.clear()
 
    pen.goto(0, 250)
 
    pen.write(
        "DAVID TURNER",
        align="center",
        font=("Arial", 24, "bold")
    )
 
    pen.goto(-250, 100)
   
    pen.write(
        "Role: Security Officer\n"
        "Experience: 8 Years\n"
        "Access Level: Very High",
        font=("Arial", 14, "normal")
    )
 
    if culprit == "David":
        statement = (
            "\"I was checking some "
            "security equipment alone.\""
        )
    else:
        statement = (
            "\"I was monitoring the "
            "security systems all afternoon.\""
        )
       
    pen.goto(-250,80)
       
    pen.write(
        statement,
        font=("Arial", 16, "normal")
    )
 
    draw_portrait_box(-100, 50)
 
    draw_face(
        -25,
        -70,
        "#F4D7B5",
        "#444444"
    )
 
    # Glasses
    pen.goto(-40, -25)
   
    pen.pendown()
    pen.circle(10)
   
    pen.penup()
   
    pen.goto(-10, -25)
   
    pen.pendown()
    pen.circle(10)
   
    pen.penup()
    pen.goto(-30, -15)
   
    pen.pendown()
    pen.goto(-20, -15)
   
    pen.penup()
 
    draw_button(
        -150,
        -220,
        300,
        60,
        "BACK"
    )
 
def show_sophie():
 
    global current_screen
    current_screen = "sophie"
 
    pen.clear()
 
    pen.goto(0, 250)
 
    pen.write(
        "SOPHIE REED",
        align="center",
        font=("Arial", 24, "bold")
    )
 
    pen.goto(-250, 100)
   
    pen.write(
        "Role: Journalist\n"
        "Experience: Investigative Reporter\n"
        "Access Level: Visitor",
        font=("Arial", 14, "normal")
    )
 
    if culprit == "Sophie":
        statement = (
            "\"I was researching a story "
            "by myself.\""
        )
    else:
        statement = (
            "\"I spent the afternoon "
            "interviewing museum visitors.\""
        )
   
    pen.goto(-250,80)
    pen.write(
        statement,
        font=("Arial", 16, "normal")
    )
 
    draw_portrait_box(-100, 50)
 
    draw_face(
        -25,
        -70,
        "#F4D7B5",
        "#D4AF37"
    )
   
    # Long hair
    pen.fillcolor("#D4AF37")
   
    pen.goto(-70, 20)
   
    pen.begin_fill()
   
    pen.goto(20, 20)
    pen.goto(20, -100)
    pen.goto(-70, -100)
    pen.goto(-70, 20)
   
    pen.end_fill()
 
    draw_face(
        -25,
        -70,
        "#F4D7B5",
        "#D4AF37"
    )
 
    draw_button(
        -150,
        -220,
        300,
        60,
        "BACK"
    )
 
def show_michael():
 
    global current_screen
    current_screen = "michael"
 
    pen.clear()
 
    pen.goto(0, 250)
 
    pen.write(
        "MICHAEL LEE",
        align="center",
        font=("Arial", 24, "bold")
    )
 
    pen.goto(-250, 100)
   
    pen.write(
        "Role: Cleaner\n"
        "Experience: 5 Years\n"
        "Access Level: Staff Areas",
        font=("Arial", 14, "normal")
    )
 
    if culprit == "Michael":
        statement = (
             "\"I was cleaning the East Wing "
             "alone at the time.\""
        )
    else:
        statement = (
            "\"I was cleaning with another "
            "staff member during the theft.\""
        )
       
    pen.goto(-250,80)
    pen.write(
        statement,
        font=("Arial", 16, "normal")
    )
 
    draw_portrait_box(-100, 50)
 
    draw_face(
        -25,
        -70,
        "#F4D7B5",
        "#222222"
    )
 
    # Cap
    pen.fillcolor("#12355B")
    pen.goto(-60, 20)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(70)
        pen.right(90)
        pen.forward(18)
        pen.right(90)
       
    pen.end_fill()
 
    pen.goto(-45, 0)
    pen.pendown()
    pen.goto(-5, 0)
    pen.penup()
    draw_button(
        -150,
        -220,
        300,
        60,
        "BACK"
    )
 
def show_evidence():
 
    global current_screen
    current_screen = "evidence"
 
    pen.clear()
 
    pen.goto(0, 250)
 
    pen.write(
        "EVIDENCE ROOM",
        align="center",
        font=("Arial", 24, "bold")
    )
   
    draw_button(-400, 150, 250, 60, "SECURITY FOOTAGE")
    draw_button(100, 150, 250, 60, "FINGERPRINTS")
    draw_button(-400, 50, 250, 60, "KEYCARD RECORDS")
    draw_button(100, 50, 250, 60, "FINANCIAL RECORDS")
    draw_button(-400, -50, 250, 60, "WITNESS STATEMENT")
    draw_button(-150, -280, 300, 60, "BACK")
 
def show_security_footage():
 
    global current_screen
    current_screen = "security"
 
    pen.clear()
 
    pen.goto(0, 250)
 
    pen.write(
        "SECURITY FOOTAGE",
        align="center",
        font=("Arial", 24, "bold")
    )
 
    pen.goto(-250, 100)
 
    pen.write(
        "The cameras stopped\n"
        "recording for 12 minutes.",
        font=("Arial", 16, "normal")
    )
   
    draw_button(
    -150,
    -100,
    300,
    60,
    "COLLECT CLUE"
    )
    draw_button(
        -150,
        -220,
        300,
        60,
        "BACK"
    )
 
def show_notebook():
 
    global current_screen
    current_screen = "notebook"
 
    pen.clear()
 
    pen.goto(0,250)
   
    pen.write(
        "DETECTIVE NOTEBOOK",
        align="center",
        font=("Arial",24,"bold")
    )
   
    pen.goto(-250, 200)
   
    pen.write(
        f"Evidence Found: {len(clues_found)}/5",
        font=("Arial",16,"bold")
    )
   
    y = 150
   
    if len(clues_found) == 0:
 
        pen.goto(-250, y)
 
        pen.write(
            "No clues found yet.",
            font=("Arial",16,"normal")
        )
 
    else:
 
        for clue in clues_found:
 
            pen.goto(-250, y)
 
            pen.write(
                "✓ " + clue,
                font=("Arial",16,"normal")
            )
 
            y -= 40
 
    draw_button(
        -150,
        -220,
        300,
        60,
        "BACK"
    )
 
def show_fingerprints():
 
    global current_screen
    current_screen = "fingerprints"
 
    pen.clear()
 
    pen.goto(0, 250)
 
    pen.write(
        "FINGERPRINTS",
        align="center",
        font=("Arial", 24, "bold")
    )
 
    pen.goto(-250, 100)
 
    pen.write(
        "Fingerprints belonging to\n"
        "Michael Lee were found.",
        font=("Arial", 16, "normal")
    )
 
    draw_button(
        -150,
        -100,
        300,
        60,
        "COLLECT CLUE"
    )
 
    draw_button(
        -150,
        -280,
        300,
        60,
        "BACK"
    )
 
def show_message(text):
 
    message_pen.clear()
 
    message_pen.goto(-250, -50)
 
    message_pen.write(
        text,
        font=("Arial", 16, "bold")
    )
 
    screen.ontimer(
        message_pen.clear,
        1250
    )
 
def show_keycard():
 
    global current_screen
    current_screen = "keycard"
 
    pen.clear()
 
    pen.goto(0, 250)
 
    pen.write(
        "KEYCARD RECORDS",
        align="center",
        font=("Arial", 24, "bold")
    )
 
    pen.goto(-250, 100)
 
    pen.write(
        f"David Turner's keycard\n"
        "entered the security room.",
        font=("Arial", 16, "normal")
    )
 
    draw_button(
        -150,
        -100,
        300,
        60,
        "COLLECT CLUE"
    )
 
    draw_button(
        -150,
        -280,
        300,
        60,
        "BACK"
    )
 
def show_financial():
 
    global current_screen
    current_screen = "financial"
 
    pen.clear()
 
    pen.goto(0, 250)
 
    pen.write(
        "FINANCIAL RECORDS",
        align="center",
        font=("Arial", 24, "bold")
    )
 
    pen.goto(-250, 100)
 
    pen.write(
        f"{full_names[culprit]} has large\n"
        "gambling debts.",
        font=("Arial", 16, "normal")
    )
 
    draw_button(
        -150,
        -100,
        300,
        60,
        "COLLECT CLUE"
    )
 
    draw_button(
        -150,
        -280,
        300,
        60,
        "BACK"
    )
 
def show_witness():
 
    global current_screen
    current_screen = "witness"
 
    pen.clear()
 
    pen.goto(0, 250)
 
    pen.write(
        "WITNESS STATEMENT",
        align="center",
        font=("Arial", 24, "bold")
    )
 
    pen.goto(-250, 100)
 
    pen.write(
        f"A witness saw {full_names[culprit]}\n"
        "carrying a backpack. They have never carried one before.",
        font=("Arial", 16, "normal")
    )
 
    draw_button(
        -150,
        -100,
        300,
        60,
        "COLLECT CLUE"
    )
 
    draw_button(
        -150,
        -280,
        300,
        60,
        "BACK"
    )
 
def show_accusation():
 
    global current_screen
    current_screen = "accusation"
 
    pen.clear()
 
    pen.goto(0, 250)
 
    pen.write(
        "WHO STOLE THE DIAMOND?",
        align="center",
        font=("Arial", 24, "bold")
    )
 
    draw_button(
        -400,
        200,
        200,
        60,
        "EMMA"
    )
 
    draw_button(
        -400,
        100,
        200,
        60,
        "DAVID"
    )
 
    draw_button(
        -400,
        0,
        200,
        60,
        "SOPHIE"
    )
 
    draw_button(
        -400,
        -100,
        200,
        60,
        "MICHAEL"
    )
 
    draw_button(
        -150,
        -280,
        300,
        60,
        "BACK"
    )
 
def win_screen():
 
    global current_screen
    current_screen = "win"
 
    pen.clear()
    draw_diamond(0, 390)
    pen.goto(0, 180)
 
    pen.write(
        "CASE SOLVED!",
        align="center",
        font=("Arial", 30, "bold")
    )
 
    pen.goto(0, 100)
 
    pen.write(
        f"The culprit was {full_names[culprit]}",
        align="center",
        font=("Arial", 16, "normal")
    )
 
    pen.goto(0, 50)
 
    pen.write(
        f"Evidence Collected: {len(clues_found)}/5",
        align="center",
        font=("Arial", 16, "normal")
    )
 
    if len(clues_found) == 5:
        rank = "RANK: MASTER DETECTIVE"
 
    elif len(clues_found) >= 4:
        rank = "RANK: EXPERT DETECTIVE"
 
    else:
        rank = "RANK: JUNIOR DETECTIVE"
 
    pen.goto(0, 0)
 
    pen.write(
        rank,
        align="center",
        font=("Arial", 18, "bold")
    )
 
    pen.goto(0, -50)
       
    pen.write(
        "Thank you for playing!",
        align="center",
        font=("Arial",14,"normal")
    )
   
    draw_button(
        -150,
        -120,
        300,
        60,
        "PLAY AGAIN"
    )
 
def lose_screen():
 
    global current_screen
    current_screen = "lose"
 
    pen.clear()
    draw_diamond(0, 390)
    pen.goto(0, 150)
 
    pen.write(
        "CASE FAILED!",
        align="center",
        font=("Arial", 30, "bold")
    )
    pen.goto(0, 100)
   
    pen.write(
        f"Evidence Collected: {len(clues_found)}/5",
        align="center",
        font=("Arial",16,"normal")
    )
 
    pen.goto(0, 70)
 
    pen.write(
        "You accused the wrong suspect.",
        align="center",
        font=("Arial", 16, "normal")
    )
 
    pen.goto(0, 20)
 
    pen.write(
        f"The real thief was\n{full_names[culprit]}.",
        align="center",
        font=("Arial", 16, "normal")
    )
 
    pen.goto(0, -50)
   
    pen.write(
        "Thank you for playing!",
        align="center",
        font=("Arial",14,"normal")
    )
 
    draw_button(
        -150,
        -120,
        300,
        60,
        "PLAY AGAIN"
    )
 
def reset_game():
 
    global clues_found
    global security_found
    global fingerprints_found
    global keycard_found
    global financial_found
    global witness_found
    global culprit
 
    clues_found = []
 
    security_found = False
    fingerprints_found = False
    keycard_found = False
    financial_found = False
    witness_found = False
 
    culprit = random.choice(suspects)
 
    show_menu()
 
def show_crime_scene():
 
    global current_screen
    current_screen = "crime"
 
    pen.clear()
 
    pen.goto(0, 250)
 
    pen.write(
        "MUSEUM MAP",
        align="center",
        font=("Arial", 24, "bold")
    )
 
    draw_button(
        -150,
        150,
        300,
        80,
        "DISPLAY CASE"
    )
 
    draw_button(
        -350,
        0,
        200,
        80,
        "SECURITY ROOM"
    )
 
    draw_button(
        150,
        0,
        200,
        80,
        "STAFF CORRIDOR"
    )
 
    draw_button(
        -150,
        -280,
        300,
        60,
        "BACK"
    )
 
def show_display_case():
 
    global current_screen
    current_screen = "display"
 
    pen.clear()
 
    pen.goto(0, 250)
 
    pen.write(
        "DISPLAY CASE",
        align="center",
        font=("Arial", 24, "bold")
    )
 
    pen.goto(-250, 100)
 
    pen.write(
        "You find fresh fingerprints\n"
        "on the glass display case.",
        font=("Arial", 16, "normal")
    )
 
    draw_button(
        -150,
        -220,
        300,
        60,
        "BACK"
    )
 
def show_security_room():
 
    global current_screen
    current_screen = "security_room"
 
    pen.clear()
 
    pen.goto(0, 250)
 
    pen.write(
        "SECURITY ROOM",
        align="center",
        font=("Arial", 24, "bold")
    )
 
    pen.goto(-250, 100)
 
    pen.write(
        "System logs confirm that\n"
        "the cameras were manually disabled.",
        font=("Arial", 16, "normal")
    )
 
    draw_button(
        -150,
        -220,
        300,
        60,
        "BACK"
    )
 
def show_staff_corridor():
 
    global current_screen
    current_screen = "corridor"
 
    pen.clear()
 
    pen.goto(0, 250)
 
    pen.write(
        "STAFF CORRIDOR",
        align="center",
        font=("Arial", 24, "bold")
    )
 
    pen.goto(-250, 100)
 
    pen.write(
        "A trail of several muddy footprints\n"
        "leads toward the security room.",
        font=("Arial", 16, "normal")
    )
 
    draw_button(
        -150,
        -220,
        300,
        60,
        "BACK"
    )
 
def show_story():
 
    global current_screen
    current_screen = "story"
 
    pen.clear()
    draw_diamond(0, 390)
    pen.goto(0, 200)
 
    pen.write(
        "THE MISSING DIAMOND",
        align="center",
        font=("Arial", 28, "bold")
    )
 
    pen.goto(-300, -60)
 
    pen.write(
        "The priceless Starfire Diamond has been stolen\n"
        "from the City Museum. Four suspects\n"
        "remain: David Turner (security guard),\n"
        "Michael Lee (cleaner), Sophie Reed (journalist) and\n"
        "Emma Brooks (museum curator). Investigate\n"
        "the crime scene, collect evidence, question suspects,\n"
        "and identify the thief.",
        font=("Arial", 16, "normal")
    )
 
    draw_button(
        -150,
        -180,
        300,
        60,
        "START INVESTIGATION"
    )
 
def draw_diamond(x, y):
 
    pen.penup()
    pen.goto(x, y)
 
    pen.pencolor("#B0FFFF")
    pen.fillcolor("#7DF9FF")
 
    pen.begin_fill()
 
    pen.pendown()
 
    pen.goto(x + 30, y - 20)
    pen.goto(x + 50, y - 50)
    pen.goto(x, y - 110)
    pen.goto(x - 50, y - 50)
    pen.goto(x - 30, y - 20)
    pen.goto(x, y)
 
    pen.end_fill()
 
    # Internal facets
 
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.goto(x, y - 110)
 
    pen.penup()
    pen.goto(x - 30, y - 20)
    pen.pendown()
    pen.goto(x, y - 50)
 
    pen.penup()
    pen.goto(x + 30, y - 20)
    pen.pendown()
    pen.goto(x, y - 50)
 
    pen.penup()
 
    # Restore gold colour
 
    pen.pencolor("#D4AF37")
# -----------------
# CLICK DETECTION
# -----------------
def mouse_click(x, y):
    print(current_screen)
    global security_found
    global fingerprints_found
    global keycard_found
    global financial_found
    global witness_found
 
    # START button on menu
    if current_screen == "menu":
 
        if -150 <= x <= 150 and -10 <= y <= 50:
            show_story()
 
    # SUSPECTS button on hub
    elif current_screen == "hub":
 
        if -350 <= x <= -100 and 40 <= y <= 100:
            show_suspects()
           
        elif 100 <= x <= 350 and 40 <= y <= 100:
            show_evidence()
 
        elif 100 <= x <= 350 and -80 <= y <= -20:
            show_notebook()
 
        elif -125 <= x <= 125 and -200 <= y <= -140:
           
            if len(clues_found) < 3:
                show_message("Collect more evidence first!")
               
            else:
                show_accusation()
 
        elif -350 <= x <= -100 and -80 <= y <= -20:
            show_crime_scene()
 
    # BACK button on suspects screen
    elif current_screen == "suspects":
        # EMMA
        if -400 <= x <= -200 and 140 <= y <= 200:
            show_emma()
       
        # DAVID
        elif -400 <= x <= -200 and 40 <= y <= 100:
            show_david()
           
        # SOPHIE
        elif -400 <= x <= -200 and -60 <= y <= 0:
            show_sophie()
           
        # MICHAEL
        elif -400 <= x <= -200 and -160 <= y <= -100:
            show_michael()
           
        # BACK
        elif -150 <= x <= 150 and -280 <= y <= -220:
            show_hub()
           
    elif current_screen == "emma":
        if -150 <= x <= 150 and -280 <= y <= -220:
            show_suspects()
           
    elif current_screen == "david":
        if -150 <= x <= 150 and -280 <= y <= -220:
            show_suspects()
           
    elif current_screen == "sophie":
        if -150 <= x <= 150 and -280 <= y <= -220:
            show_suspects()
           
    elif current_screen == "michael":
        if -150 <= x <= 150 and -280 <= y <= -220:
            show_suspects()
   
    elif current_screen == "evidence":
        # Security Footage
        if -400 <= x <= -150 and 90 <= y <= 150:
            show_security_footage()
       
        # Back
        elif -150 <= x <= 150 and -340 <= y <= -280:
            show_hub()
 
        elif 100 <= x <= 350 and 90 <= y <= 150:
            print("OPENING FINGERPRINTS")
            show_fingerprints()
 
        elif -400 <= x <= -150 and -10 <= y <= 50:
            show_keycard()
 
        elif 100 <= x <= 350 and -10 <= y <= 50:
            show_financial()
 
        elif -300 <= x <= 0 and -110 <= y <= -50:
            show_witness()
 
    elif current_screen == "security":
       
        # COLLECT CLUE
       
        if -150 <= x <= 150 and -160 <= y <= -100:
           
            print("COLLECT CLICKED")
           
            if not security_found:
                clues_found.append("Camera Outage")
                security_found = True
               
                show_message("✓ Clue Added!")
               
        # BACK
        elif -150 <= x <= 150 and -280 <= y <= -220:
            show_evidence()
 
    elif current_screen == "notebook":
        if -150 <= x <= 150 and -280 <= y <= -220:
            show_hub()
 
    elif current_screen == "fingerprints":
       
        if -150 <= x <= 150 and -160 <= y <= -100:
           
            if not fingerprints_found:
                clues_found.append("Fingerprints")
                fingerprints_found = True
               
                show_message("✓ Clue Added!")
           
        elif -150 <= x <= 150 and -340 <= y <= -280:
            show_evidence()
 
    elif current_screen == "keycard":
        if -150 <= x <= 150 and -160 <= y <= -100:
            if not keycard_found:
               
                clues_found.append("Keycard Records")
                keycard_found = True
               
                show_message("✓ Clue Added!")
               
        elif -150 <= x <= 150 and -340 <= y <= -280:
           
            show_evidence()
 
    elif current_screen == "financial":
           
        if -150 <= x <= 150 and -160 <= y <= -100:
               
            if not financial_found:
                   
                clues_found.append("Financial Records")
                financial_found = True
                   
                show_message("✓ Clue Added!")
                   
        elif -150 <= x <= 150 and -340 <= y <= -280:
            show_evidence()
 
    elif current_screen == "witness":
        if -150 <= x <= 150 and -160 <= y <= -100:
            if not witness_found:
                clues_found.append("Witness Statement")
                witness_found = True
               
                show_message("✓ Clue Added!")
               
        elif -150 <= x <= 150 and -340 <= y <= -280:
           
            show_evidence()
 
    elif current_screen == "accusation":
       
        # EMMA
        if -400 <= x <= -200 and 140 <= y <= 200:
            if culprit == "Emma":
                win_screen()
           
            else:
                lose_screen()
               
        # DAVID
        elif -400 <= x <= -200 and 40 <= y <= 100:
            if culprit == "David":
                win_screen()
               
            else:
                lose_screen()
               
        # SOPHIE
        elif -400 <= x <= -200 and -60 <= y <= 0:
            if culprit == "Sophie":
                win_screen()
               
            else:
                lose_screen()
               
        # MICHAEL
        elif -400 <= x <= -200 and -160 <= y <= -100:
            if culprit == "Michael":
                win_screen()
               
            else:
                lose_screen()
           
        # BACK
        elif -150 <= x <= 150 and -340 <= y <= -280:
            show_hub()
 
    elif current_screen == "win":
        if -150 <= x <= 150 and -180 <= y <= -120:
            reset_game()
           
    elif current_screen == "lose":
        if -150 <= x <= 150 and -180 <= y <= -120:
            reset_game()
 
    elif current_screen == "crime":
        # DISPLAY CASE
        if -150 <= x <= 150 and 70 <= y <= 150:
            show_display_case()
           
        # SECURITY ROOM
        elif -350 <= x <= -150 and -80 <= y <= 0:
            show_security_room()
           
        # STAFF CORRIDOR
        elif 150 <= x <= 350 and -80 <= y <= 0:
            show_staff_corridor()
           
        # BACK
        elif -150 <= x <= 150 and -340 <= y <= -280:
            show_hub()
 
    elif current_screen == "display":
        if -150 <= x <= 150 and -280 <= y <= -220:
            show_crime_scene()
       
    elif current_screen == "security_room":
        if -150 <= x <= 150 and -280 <= y <= -220:
            show_crime_scene()
           
    elif current_screen == "corridor":
        if -150 <= x <= 150 and -280 <= y <= -220:
            show_crime_scene()
 
    elif current_screen == "story":
        if -150 <= x <= 150 and -240 <= y <= -180:
            show_hub()
 
# Start game
show_menu()
 
screen.onclick(mouse_click)
 
screen.mainloop()
