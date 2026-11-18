import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import random
import math
import time
import json
import os
from datetime import datetime

# ZERO TO HERO — educational fictional investing simulator
# Runs with Python's standard library; no pip installs required.

STARTING_STOCKS = [
    ("NovaDrive Motors", "NDM", "Electric Vehicles", 42.80, "Rising", "High"),
    ("CloudCore Systems", "CCS", "Technology", 87.50, "Rising", "Medium-High"),
    ("FreshFork Foods", "FFF", "Food & Agriculture", 18.25, "Declining", "Low"),
    ("TitanForge Industries", "TFI", "Manufacturing", 63.40, "Rising", "Low"),
    ("BlueWave Energy", "BWE", "Renewable Energy", 31.70, "Rising", "Medium"),
    ("Medivance Health", "MVH", "Healthcare", 74.90, "Declining", "Medium"),
    ("PixelPeak Games", "PPG", "Gaming", 12.60, "Rising", "Very High"),
    ("IronRock Mining", "IRM", "Mining", 55.30, "Declining", "High"),
    ("SkyLink Aviation", "SLA", "Aviation", 29.45, "Rising", "Medium-High"),
    ("NeonByte Cybersecurity", "NBC", "Cybersecurity", 96.20, "Declining", "High"),
    ("AquaPure Technologies", "APT", "Water Technology", 24.80, "Rising", "Low"),
    ("RavenBank Financial", "RBF", "Banking", 68.15, "Rising", "Low"),
    ("HyperHaul Logistics", "HHL", "Transportation", 36.40, "Declining", "Medium"),
    ("Solaris Power", "SLP", "Energy", 51.75, "Rising", "Medium-High"),
    ("Vortex Robotics", "VTX", "Robotics & AI", 15.90, "Rising", "Very High"),
    ("GoldenGrain Corp", "GGC", "Agriculture", 43.60, "Declining", "Low"),
    ("UrbanNest Properties", "UNP", "Real Estate", 72.30, "Declining", "Medium"),
    ("QuantumEdge Labs", "QEL", "Biotechnology", 8.75, "Rising", "Extreme"),
    ("Starlight Media", "STM", "Entertainment", 27.50, "Declining", "Medium-High"),
    ("Atlas Defence Systems", "ADS", "Aerospace & Defence", 91.80, "Rising", "Medium"),
    ("CopperPeak Resources", "CPR", "Mining", 34.60, "Rising", "High"),
    ("Evergreen Waterworks", "EWW", "Water Technology", 22.40, "Rising", "Low"),
    ("BrightPath Education", "BPE", "Education", 16.80, "Rising", "Medium"),
    ("Northstar Telecom", "NST", "Telecommunications", 48.20, "Declining", "Medium"),
    ("SwiftCart Retail", "SCR", "Retail", 39.75, "Rising", "Medium-High"),
    ("HarvestMoon Grocers", "HMG", "Food & Agriculture", 28.30, "Rising", "Low"),
    ("PulseFit Athletics", "PFA", "Sports & Fitness", 19.60, "Rising", "High"),
    ("CloudNine Travel", "CNT", "Travel & Tourism", 44.10, "Declining", "High"),
    ("CivicBuild Infrastructure", "CBI", "Construction", 57.90, "Rising", "Medium"),
    ("LumenGrid Utilities", "LGU", "Utilities", 62.15, "Rising", "Low"),
    ("FrostByte Computing", "FBC", "Technology", 113.40, "Rising", "Very High"),
    ("OrchardVale Produce", "OVP", "Agriculture", 14.25, "Declining", "Medium"),
    ("Silverline Insurance", "SLI", "Insurance", 71.80, "Rising", "Low"),
    ("Redwood Capital Group", "RCG", "Investment Services", 83.50, "Declining", "Medium-High"),
    ("Petal & Pine Brands", "PPB", "Consumer Goods", 25.70, "Rising", "Medium"),
    ("DeepCurrent Shipping", "DCS", "Shipping", 31.25, "Declining", "High"),
    ("Moonshot Aerospace", "MSA", "Aerospace & Defence", 67.30, "Rising", "Very High"),
    ("Kindred Care Network", "KCN", "Healthcare", 36.90, "Rising", "Low"),
    ("EchoStream Audio", "ESA", "Entertainment", 11.40, "Declining", "High"),
    ("TerraVolt Batteries", "TVB", "Electric Vehicles", 52.60, "Rising", "Very High"),
    ("Summit Hotels Group", "SHG", "Travel & Tourism", 46.75, "Rising", "Medium-High"),
    ("BluePeak Insurance", "BPI", "Insurance", 29.90, "Declining", "Medium"),
    ("GreenCanopy Forestry", "GCF", "Forestry", 17.55, "Rising", "High"),
    ("Asterion Semiconductors", "AST", "Semiconductors", 124.80, "Rising", "Extreme"),
    ("MetroLink Transit", "MLT", "Transportation", 40.20, "Rising", "Medium"),
    ("Little Lantern Toys", "LLT", "Consumer Goods", 9.85, "Declining", "High"),
    ("Pioneer BioLabs", "PBL", "Biotechnology", 21.30, "Rising", "Extreme"),
    ("Stonebridge Materials", "SBM", "Construction", 58.60, "Declining", "Medium-High"),
    ("Aurora Solarworks", "ASW", "Renewable Energy", 33.45, "Rising", "High"),
    ("Ironclad Cyber Defence", "ICD", "Cybersecurity", 64.20, "Rising", "High"),
]
# Daily price volatility. High-risk stocks can move dramatically in a single game day.
# Extreme stocks have a 22% standard deviation before occasional jump/crash events.
RISK_VOL = {"Low": .015, "Medium": .03, "Medium-High": .055, "High": .085, "Very High": .13, "Extreme": .22}
SECTOR_EVENTS = [
    ("Clean-energy subsidies announced", "Renewable Energy", .13),
    ("A major data-centre boom lifts demand", "Technology", .12),
    ("New medical breakthrough reported", "Healthcare", .14),
    ("Cyberattack raises security spending", "Cybersecurity", .15),
    ("A shipping bottleneck disrupts deliveries", "Transportation", -.13),
    ("Fuel prices jump unexpectedly", "Aviation", -.12),
    ("A bumper harvest eases food prices", "Food & Agriculture", -.08),
    ("New battery technology excites investors", "Electric Vehicles", .16),
    ("Interest rates rise, worrying borrowers", "Banking", -.10),
    ("A robotics company reveals a major advance", "Robotics & AI", .18),
    ("A mining accident halts production", "Mining", -.16),
    ("A hit game breaks sales records", "Gaming", .17),
    ("Factory automation boosts manufacturers", "Manufacturing", .10),
    ("Water shortages increase demand for treatment", "Water Technology", .13),
    ("A property downturn spooks investors", "Real Estate", -.14),
    ("Defence contracts increase after global tensions", "Aerospace & Defence", .12),
    ("Advertisers cut spending", "Entertainment", -.10),
    ("A new crop disease worries farmers", "Agriculture", -.12),
    ("Oil prices swing after a surprise announcement", "Energy", -.09),
    ("Markets react nervously to world headlines", "ALL", -.035),
    ("Inflation cools and markets rally", "ALL", .045),
    ("Unexpected trade restrictions disrupt supply chains", "ALL", -.055),
]
LIFE_EVENTS = [
    {"title":"Unexpected medical bill", "desc":"A surprise $650 bill arrives. You need to deal with it before moving on.", "options":[("Pay $650 cash", "pay", 650, None), ("Borrow $650 to cover it", "borrow", 650, None)]},
    {"title":"Your laptop breaks", "desc":"A replacement costs $800. You need it for work and study.", "options":[("Pay $800 cash", "pay", 800, None), ("Take an $800 loan", "borrow", 800, None)]},
    {"title":"Freelance opportunity", "desc":"A local business offers you a small paid project. You can take the safe payment or spend money trying to scale it.", "options":[("Take the $350 guaranteed payment", "gain", 350, None), ("Risk $250 on a bigger project", "risky", 250, None), ("Pass", "skip", 0, None)]},
    {"title":"A surprise refund", "desc":"A company admits it overcharged you and sends a refund. You can keep it or use it to reduce your debt.", "options":[("Keep the $450 refund", "gain", 450, None), ("Use $450 to reduce debt", "debtpay", 450, None)]},
    {"title":"Startup pitch", "desc":"A friend wants you to invest in a tiny startup. It might pay off, but you could lose the stake.", "options":[("Invest $300 (high risk)", "risky", 300, None), ("Keep your cash safe", "skip", 0, None)]},
    {"title":"Cybersecurity boom", "desc":"Demand for cybersecurity firms surges after a major data breach. Your choice can move the whole sector.", "options":[("Ride the market wave (+8% sector shock)", "market", 0, ("Cybersecurity", .08)), ("Stay cautious", "skip", 0, None)]},
    {"title":"Market panic", "desc":"Investors panic after worrying economic news. It could be a buying opportunity, but prices may remain volatile.", "options":[("Brace for a market dip (-5% overall)", "market", 0, ("ALL", -.05)), ("Ignore the noise", "skip", 0, None)]},
    {"title":"Dividend surprise", "desc":"A group of mature companies announces a special simulated dividend for investors.", "options":[("Collect $200 cash", "gain", 200, None), ("Pass on the payout", "skip", 0, None)]},
    {"title":"Fake investment message", "desc":"A message promises guaranteed returns if you send money now. It looks suspicious. Decide how to respond.", "options":[("Report it and pay $50 admin cost", "pay", 50, None), ("Ignore it safely", "skip", 0, None), ("Fall for it (lose up to $300)", "loss", 300, None)]},
    {"title":"Skills course", "desc":"A short course could help your future earning potential, but it costs $250 today.", "options":[("Pay $250 for the course", "pay", 250, None), ("Skip the course", "skip", 0, None)]},
    {"title":"Family celebration", "desc":"You are invited to a family event. You can contribute, or politely keep your budget intact.", "options":[("Contribute $180", "pay", 180, None), ("Keep your money", "skip", 0, None)]},
    {"title":"Clean-energy breakthrough", "desc":"A breakthrough boosts confidence in renewable energy companies. The sector could jump, but nothing is guaranteed.", "options":[("Apply a +7% sector shock", "market", 0, ("Renewable Energy", .07)), ("Do nothing", "skip", 0, None)]},
    {"title":"Insurance renewal", "desc":"Your annual insurance is due. Paying now avoids a larger penalty later.", "options":[("Pay $400 premium", "pay", 400, None), ("Borrow $400 to cover it", "borrow", 400, None)]},
    {"title":"Unexpected tax refund", "desc":"A fictional tax adjustment works in your favour. You receive a modest refund.", "options":[("Claim $300 refund", "gain", 300, None), ("Leave it unclaimed", "skip", 0, None)]},
    {"title":"Supply-chain shock", "desc":"A disruption hits transport and shipping companies. You can accept the news or try not to overreact.", "options":[("Apply a -7% transport shock", "market", 0, ("Transportation", -.07)), ("Stay the course", "skip", 0, None)]},
]

COUNTRY_TAX = [
    ("Australia", "Tax depends on residency, income, and how the gain is made."),
    ("United States", "Federal and state tax can apply; rates depend on holding period and location."),
    ("United Kingdom", "Capital Gains Tax rules and allowances may apply."),
    ("New Zealand", "Tax treatment depends on why assets were acquired and other circumstances."),
    ("Canada", "Capital gains are generally treated under federal and provincial rules."),
]

BG = "#0b1220"
PANEL = "#121d30"
PANEL2 = "#19283e"
BORDER = "#263a54"
TEXT = "#edf4ff"
MUTED = "#93a7c2"
TEAL = "#43e0c0"
BLUE = "#65a7ff"
RED = "#ff7185"
GOLD = "#ffd166"
GREEN = "#64e59a"

class ZeroToHero:
    def __init__(self, root):
        self.root = root
        self.root.title("ZERO TO HERO | Money choices, real consequences")
        self.root.geometry("1180x780")
        self.root.minsize(980, 680)
        self.root.configure(bg=BG)
        self.style = ttk.Style()
        try: self.style.theme_use("clam")
        except tk.TclError: pass
        self.style.configure("Treeview", background=PANEL, foreground=TEXT, fieldbackground=PANEL,
                             rowheight=30, borderwidth=0, font=("Segoe UI", 10))
        self.style.configure("Treeview.Heading", background=PANEL2, foreground=MUTED,
                             font=("Segoe UI", 9, "bold"), relief="flat")
        self.style.map("Treeview", background=[("selected", "#244d68")], foreground=[("selected", TEXT)])
        self.player_name = "Investor"
        self.difficulty = "Medium"
        self.day = 1
        self.age = 18
        self.cash = 1000.0
        self.loan = 0.0
        # New asset systems. All monetary values are rounded to cents at transaction boundaries.
        self.properties = []
        self.businesses = []
        self.fund_holdings = {"GROW": 0.0, "BOND": 0.0, "GOLD": 0.0}
        self.fund_prices = {"GROW": 100.0, "BOND": 100.0, "GOLD": 50.0}
        self.fund_history = {k: [v] for k, v in self.fund_prices.items()}
        self.side_hustle_day = {}
        self.achievements = set()
        self.claimed_missions = set()
        self.stocks = {}
        for name, ticker, sector, price, trend, risk in STARTING_STOCKS:
            self.stocks[ticker] = {"name": name, "sector": sector, "price": price,
                "trend": trend, "risk": risk, "history": [price], "fee": .025 if risk in ("Low","Medium") else .04}
        # Stock-price history is kept between games and saved beside this script.
        self.history_file = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "zero_to_hero_stock_history.json"
        )
        self._load_stock_history()
        self.holdings = {t: 0.0 for t in self.stocks}
        self.news_log = []
        self.portfolio_history = [1000.0]
        self.victory_shown = False
        self.day_seconds = 8
        self.last_tick = time.time()
        self.running = False
        self.paused = False
        self.selected_ticker = "NDM"
        self.withdrawal_blocked_today = False
        self.last_event = None
        self.current_event = None
        self.screen = "menu"
        self.show_menu()
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        """Save persistent market history once when the user exits."""
        self._save_stock_history()
        self.root.destroy()

    def clear(self):
        for w in self.root.winfo_children(): w.destroy()
        self.root.configure(bg=BG)

    def frame(self, parent=None, bg=BG, **kw):
        return tk.Frame(parent or self.root, bg=bg, **kw)

    def label(self, parent, text, size=11, color=TEXT, bold=False, **kw):
        return tk.Label(parent, text=text, bg=parent.cget("bg"), fg=color,
                        font=("Segoe UI", size, "bold" if bold else "normal"), **kw)

    def button(self, parent, text, command, primary=False, **kw):
        # Allow individual buttons to override sizing/font without duplicate kwargs.
        options = {
            "bg": TEAL if primary else PANEL2,
            "fg": BG if primary else TEXT,
            "activebackground": BLUE,
            "activeforeground": BG,
            "relief": "flat",
            "bd": 0,
            "padx": 18,
            "pady": 10,
            "cursor": "hand2",
            "font": ("Segoe UI", 10, "bold"),
        }
        options.update(kw)
        return tk.Button(parent, text=text, command=command, **options)

    def panel(self, parent, title=None):
        p = self.frame(parent, bg=PANEL, highlightbackground=BORDER, highlightthickness=1)
        if title:
            self.label(p, title.upper(), 9, MUTED, True).pack(anchor="w", padx=16, pady=(13, 8))
        return p

    def header(self, title, subtitle=""):
        top = self.frame(self.root, bg=BG)
        top.pack(fill="x", padx=26, pady=(22, 12))
        self.label(top, "ZERO / TO / HERO", 10, TEAL, True).pack(anchor="w")
        self.label(top, title, 25, TEXT, True).pack(anchor="w", pady=(5, 1))
        if subtitle: self.label(top, subtitle, 10, MUTED).pack(anchor="w")
        return top

    def _load_stock_history(self):
        """Load saved price histories if the JSON file exists."""
        try:
            with open(self.history_file, "r", encoding="utf-8") as file:
                saved = json.load(file)
            for ticker, stock in self.stocks.items():
                item = saved.get(ticker, {})
                history = item.get("history", [])
                if isinstance(history, list):
                    clean_history = []
                    for value in history:
                        try:
                            number = float(value)
                            if math.isfinite(number) and number > 0:
                                clean_history.append(number)
                        except (TypeError, ValueError):
                            continue
                    if clean_history:
                        # Keep a useful chart history without allowing memory use to grow forever.
                        stock["history"] = clean_history[-1000:]
                        stock["price"] = stock["history"][-1]
                if item.get("trend") in ("Rising", "Declining"):
                    stock["trend"] = item["trend"]
        except (OSError, json.JSONDecodeError, AttributeError, TypeError):
            # A missing or damaged history file should never stop the game.
            pass

    def _save_stock_history(self):
        """Save price history in a compact JSON file beside the Python script."""
        try:
            saved = {
                ticker: {
                    "price": round(float(stock["price"]), 4),
                    "trend": stock.get("trend", "Rising"),
                    "history": [round(float(value), 4) for value in stock.get("history", [])[-1000:]]
                }
                for ticker, stock in self.stocks.items()
            }
            temporary_file = self.history_file + ".tmp"
            with open(temporary_file, "w", encoding="utf-8") as file:
                json.dump(saved, file, indent=2)
            os.replace(temporary_file, self.history_file)
        except (OSError, TypeError, ValueError):
            # The simulator remains playable if the folder is read-only.
            pass

    def show_menu(self):
        self.screen = "menu"; self.clear()
        outer = self.frame(); outer.pack(fill="both", expand=True, padx=54, pady=36)
        self.label(outer, "ZERO / TO / HERO", 12, TEAL, True).pack(anchor="w", pady=(5, 24))
        hero = self.frame(outer, bg=BG); hero.pack(fill="both", expand=True)
        self.label(hero, "YOUR MONEY.\nYOUR MOVES.\nYOUR FUTURE.", 36, TEXT, True, justify="left").pack(anchor="w", pady=(45, 12))
        self.label(hero, "A market simulator where every decision changes your story.", 13, MUTED).pack(anchor="w")
        stats = self.frame(hero, bg=BG); stats.pack(anchor="w", pady=26)
        for value, caption in [("$1,000", "STARTING CASH"), (str(len(STARTING_STOCKS)), "FICTIONAL STOCKS"), ("$1M", "THE MISSION")]:
            card = self.frame(stats, bg=PANEL, padx=18, pady=14, highlightbackground=BORDER, highlightthickness=1)
            card.pack(side="left", padx=(0, 12))
            self.label(card, value, 19, TEAL, True).pack(anchor="w")
            self.label(card, caption, 8, MUTED, True).pack(anchor="w", pady=(4,0))
        actions = self.frame(outer, bg=BG); actions.pack(anchor="w", pady=18)
        self.button(actions, "PLAY GAME  →", self.create_character, True, width=18).pack(side="left", padx=(0,10))
        self.button(actions, "HOW TO PLAY", self.how_to_play).pack(side="left", padx=5)
        self.button(actions, "SETTINGS", self.settings).pack(side="left", padx=5)
        self.label(outer, "Educational simulation only • All companies and prices are fictional", 9, MUTED).pack(anchor="w", pady=(18,0))

    def create_character(self):
        self.clear(); self.screen = "character"
        self.header("Create your character", "Choose a name and a market difficulty.")
        card = self.panel(self.root); card.pack(fill="x", padx=28, pady=12)
        self.label(card, "WHAT SHOULD WE CALL YOU?", 10, MUTED, True).pack(anchor="w", padx=20, pady=(20,6))
        self.name_entry = tk.Entry(card, font=("Segoe UI", 13), bg=PANEL2, fg=TEXT, insertbackground=TEXT, relief="flat")
        self.name_entry.insert(0, self.player_name); self.name_entry.pack(fill="x", padx=20, ipady=9)
        self.label(card, "DIFFICULTY", 10, MUTED, True).pack(anchor="w", padx=20, pady=(22,8))
        self.diff_var = tk.StringVar(value=self.difficulty)
        row = self.frame(card, bg=PANEL); row.pack(anchor="w", padx=20, pady=(0,20))
        for d, desc in [("Easy","Smaller market swings"),("Medium","Balanced volatility"),("Hard","Bigger risks, bigger swings")]:
            box = self.frame(row, bg=PANEL2, padx=12, pady=10); box.pack(side="left", padx=(0,8))
            tk.Radiobutton(box, text=d, variable=self.diff_var, value=d, bg=PANEL2, fg=TEXT,
                selectcolor=BG, activebackground=PANEL2, activeforeground=TEXT).pack(anchor="w")
            self.label(box, desc, 8, MUTED).pack(anchor="w", padx=4)
        self.button(self.root, "START MY STORY  →", self.start_game, True).pack(anchor="w", padx=28, pady=14)
        self.button(self.root, "← BACK", self.show_menu).pack(anchor="w", padx=28)

    def start_game(self):
        self.player_name = self.name_entry.get().strip() or "Investor"
        self.difficulty = self.diff_var.get()
        self.day = 1; self.age = 18; self.cash = 1000.0; self.loan = 0.0
        self.properties = []; self.businesses = []
        self.fund_holdings = {"GROW": 0.0, "BOND": 0.0, "GOLD": 0.0}
        self.fund_prices = {"GROW": 100.0, "BOND": 100.0, "GOLD": 50.0}
        self.fund_history = {k: [v] for k, v in self.fund_prices.items()}
        self.side_hustle_day = {}; self.achievements = set(); self.claimed_missions = set()
        self.holdings = {t: 0.0 for t in self.stocks}
        self.portfolio_history = [1000.0]; self.news_log = []
        self.victory_shown = False
        # Each new game starts with the original prices, while the chart keeps
        # all previously saved observations and adds this game's starting point.
        starting_prices = {row[1]: row[3] for row in STARTING_STOCKS}
        for ticker, stock in self.stocks.items():
            stock["price"] = starting_prices[ticker]
            stock["trend"] = next(row[4] for row in STARTING_STOCKS if row[1] == ticker)
            stock.setdefault("history", []).append(stock["price"])
        self._save_stock_history()
        self.running = True; self.paused = False; self.last_tick = time.time()
        # Keep the pace chosen in Settings; default is a fast 8-second day.
        self.advance_day(initial=True)
        self.dashboard()

    def how_to_play(self):
        self.clear(); self.screen = "help"
        self.header("How to play", "Learn the loop before you risk your virtual money.")
        steps = [
            ("01", "INVEST", "Buy fractional shares in fictional companies. Diversification can reduce concentration risk."),
            ("02", "FOLLOW THE NEWS", "A daily event can move a sector or the whole market. Prices can rise or fall."),
            ("03", "CHECK YOUR HISTORY", "Past performance is useful context, not a guarantee of future results."),
            ("04", "PREPARE FOR EVERY 5TH DAY", "A choice-driven life event arrives every five days, so keep some cash available."),
            ("05", "REACH $1,000,000", "Your target is total net worth: cash plus the current value of your investments."),
        ]
        for num, title, body in steps:
            row = self.panel(self.root); row.pack(fill="x", padx=28, pady=5)
            self.label(row, num, 16, TEAL, True).pack(side="left", padx=18, pady=13)
            inner = self.frame(row, bg=PANEL); inner.pack(side="left", fill="x", expand=True, padx=(0,12), pady=10)
            self.label(inner, title, 10, TEXT, True).pack(anchor="w")
            self.label(inner, body, 9, MUTED, wraplength=850, justify="left").pack(anchor="w", pady=(3,0))
        self.button(self.root, "BACK TO MENU", self.show_menu).pack(anchor="w", padx=28, pady=14)

    def settings(self):
        self.clear(); self.screen = "settings"
        self.header("Settings", "Adjust how quickly the fictional days pass.")
        card = self.panel(self.root, "Game pace"); card.pack(fill="x", padx=28, pady=10)
        self.pace_var = tk.IntVar(value=self.day_seconds)
        for secs, text in [(5,"5 seconds (chaos mode)"),(8,"8 seconds (fast)"),(15,"15 seconds (relaxed)")]:
            tk.Radiobutton(card, text=text, variable=self.pace_var, value=secs, bg=PANEL, fg=TEXT,
                selectcolor=PANEL2, activebackground=PANEL, activeforeground=TEXT,
                font=("Segoe UI", 11)).pack(anchor="w", padx=18, pady=6)
        self.button(self.root, "SAVE SETTINGS", self.save_settings, True).pack(anchor="w", padx=28, pady=12)
        self.button(self.root, "BACK", self.show_menu).pack(anchor="w", padx=28)

    def save_settings(self):
        self.day_seconds = self.pace_var.get()
        messagebox.showinfo("Settings saved", "Your day length is set to {} seconds. It will apply to your next game.".format(self.day_seconds))
        self.show_menu()

    def net_worth(self):
        stock_value = sum(self.holdings[t] * self.stocks[t]["price"] for t in self.stocks)
        fund_value = sum(self.fund_holdings[k] * self.fund_prices[k] for k in self.fund_holdings)
        property_equity = sum(p["value"] - p["mortgage"] for p in self.properties)
        business_value = sum(b["value"] for b in self.businesses)
        return round(self.cash + stock_value + fund_value + property_equity + business_value - self.loan, 2)

    def advance_day(self, initial=False, show_event=True):
        if not initial:
            self.day += 1
            self.age = 18 + (self.day - 1) // 365
            # Interest is charged on outstanding debt each game day.
            if self.loan > 0:
                self.loan = round(self.loan * 1.0015, 2)
            # Simulated daily returns for diversified investments; bonds are steadier.
            for code, base_vol, drift in (("GROW", .012, .00035), ("BOND", .0018, .00012), ("GOLD", .018, .0001)):
                change = random.gauss(drift, base_vol)
                self.fund_prices[code] = round(max(1.0, self.fund_prices[code] * (1 + change)), 2)
                self.fund_history[code].append(self.fund_prices[code])
                if len(self.fund_history[code]) > 1000:
                    del self.fund_history[code][:-1000]
            # Property values drift with the simulated market; businesses can also be revalued.
            for prop in self.properties:
                prop["value"] = round(max(1000.0, prop["value"] * (1 + random.gauss(.0002, .0025))), 2)
            for biz in self.businesses:
                biz["value"] = round(max(100.0, biz["value"] * (1 + random.gauss(.0003, .003))), 2)
            # Properties collect rent and pay maintenance every 10 game days.
            if self.day % 10 == 0:
                for prop in self.properties:
                    rent = prop["rent"]
                    mortgage_interest = prop["mortgage"] * .006
                    maintenance = prop["value"] * .0015
                    self.cash = round(self.cash + rent - mortgage_interest - maintenance, 2)
                    prop["mortgage"] = round(max(0, prop["mortgage"] + mortgage_interest - min(rent * .25, prop["mortgage"])), 2)
                for biz in self.businesses:
                    self.cash = round(self.cash + biz["income"], 2)
            difficulty_mult = {"Easy": .68, "Medium": 1.0, "Hard": 1.35}[self.difficulty]
            for ticker, stock in self.stocks.items():
                vol = RISK_VOL[stock["risk"]] * difficulty_mult
                drift = .002 if stock["trend"] == "Rising" else -.001
                change = random.gauss(drift, vol)
                # High-risk companies occasionally experience a major earnings surprise,
                # product breakthrough, scandal, or funding scare.
                jump_chance = {"Low": 0.005, "Medium": 0.01, "Medium-High": 0.025,
                               "High": 0.04, "Very High": 0.07, "Extreme": 0.12}[stock["risk"]]
                if random.random() < jump_chance:
                    jump_size = {"Low": 0.04, "Medium": 0.07, "Medium-High": 0.12,
                                 "High": 0.18, "Very High": 0.28, "Extreme": 0.45}[stock["risk"]]
                    change += random.choice((-1, 1)) * random.uniform(jump_size * 0.5, jump_size)
                # Prevent a single simulated day from taking a stock below zero or
                # producing a mathematically impossible loss greater than 100%.
                change = max(-0.90, min(1.50, change))
                stock["price"] = max(.25, stock["price"] * (1 + change))
                stock["history"].append(stock["price"])
                if len(stock["history"]) > 1000:
                    del stock["history"][:-1000]
                stock["trend"] = "Rising" if change >= 0 else "Declining"

        # A normal daily headline moves the market; every fifth day can trigger a
        # choice-driven life event rather than an automatic fine.
        event = random.choice(SECTOR_EVENTS)
        self.last_event = event
        headline, sector, impact = event
        self.apply_market_event(sector, impact)
        self.news_log.insert(0, (self.day, headline, sector, impact))
        self.news_log = self.news_log[:30]
        self.portfolio_history.append(self.net_worth())
        if len(self.portfolio_history) > 1000:
            del self.portfolio_history[:-1000]
        self.withdrawal_blocked_today = (self.day % 5 == 0 and not initial)
        self.last_tick = time.time()
        # Writing the full history JSON every game day gets increasingly expensive.
        # Save periodically and on exit instead.
        if self.day % 25 == 0:
            self._save_stock_history()
        if self.running and not self.victory_shown and self.net_worth() >= 1_000_000:
            self.victory()
            return
        if self.withdrawal_blocked_today:
            self.current_event = random.choice(LIFE_EVENTS)
            if show_event:
                self.root.after(200, self.emergency_popup)

    def apply_market_event(self, sector, impact):
        for ticker, stock in self.stocks.items():
            if sector == "ALL" or stock["sector"] == sector:
                stock["price"] = max(.25, stock["price"] * (1 + impact * random.uniform(.65, 1.15)))
                if stock["history"]:
                    stock["history"][-1] = stock["price"]
                else:
                    stock["history"].append(stock["price"])

    def emergency_popup(self):
        if self.screen not in ("dashboard", "market", "portfolio", "history", "news", "property", "business", "advanced", "missions"):
            return
        event = self.current_event
        if not event:
            return
        win = tk.Toplevel(self.root)
        win.title("Day %d challenge" % self.day)
        win.configure(bg=PANEL)
        win.geometry("540x390")
        win.transient(self.root)
        win.grab_set()
        win.protocol("WM_DELETE_WINDOW", lambda: None)  # Make a choice to continue.
        self.label(win, "DAY %d  •  LIFE EVENT" % self.day, 10, GOLD, True).pack(anchor="w", padx=22, pady=(20,8))
        self.label(win, event["title"], 21, TEXT, True, wraplength=490, justify="left").pack(anchor="w", padx=22)
        self.label(win, event["desc"], 10, MUTED, wraplength=490, justify="left").pack(anchor="w", padx=22, pady=(10,16))
        self.label(win, "Cash: ${:,.2f}     Debt: ${:,.2f}".format(self.cash, self.loan), 10, TEAL, True).pack(anchor="w", padx=22)
        buttons = self.frame(win, bg=PANEL)
        buttons.pack(fill="x", padx=22, pady=18)
        for label, action, value, extra in event["options"]:
            self.button(buttons, label, lambda a=action, v=value, x=extra: self.resolve_life_event(a, v, x, win), primary=(action in ("pay", "gain", "market"))).pack(fill="x", pady=4)

    def resolve_life_event(self, action, value, extra, win):
        # Every option has a real consequence. Bills cannot be dismissed and
        # borrowed money is recorded as debt, never free cash.
        if action == "pay":
            if self.cash < value:
                messagebox.showwarning("Not enough cash", "You need ${:,.2f} but only have ${:,.2f}. Choose the loan option or another available choice.".format(value, self.cash), parent=win)
                return
            self.cash = round(self.cash - value, 2)
            result = "Paid ${:,.2f} from cash.".format(value)
        elif action == "borrow":
            self.loan = round(self.loan + value, 2)
            result = "Borrowed ${:,.2f}. It covers the bill, but your debt is now ${:,.2f}. Interest accrues each game day.".format(value, self.loan)
        elif action == "debtpay":
            if self.loan <= 0:
                self.cash = round(self.cash + value, 2)
                result = "You have no debt, so the $450 stays in your cash balance."
            else:
                if self.cash < value:
                    messagebox.showwarning("Not enough cash", "You need ${:,.2f} in available cash to make this repayment.".format(value), parent=win)
                    return
                paid = min(value, self.loan)
                self.cash = round(self.cash - paid, 2)
                self.loan = round(max(0.0, self.loan - paid), 2)
                result = "Repaid ${:,.2f} of debt. Remaining debt: ${:,.2f}.".format(paid, self.loan)
        elif action == "gain":
            self.cash = round(self.cash + value, 2)
            result = "You received ${:,.2f}.".format(value)
        elif action == "loss":
            loss = min(self.cash, value)
            self.cash = round(self.cash - loss, 2)
            result = "You lost ${:,.2f} in cash.".format(loss)
        elif action == "market":
            sector, impact = extra
            self.apply_market_event(sector, impact)
            result = "The %s sector moved by about %+.1f%%." % (sector, impact * 100)
            self.news_log.insert(0, (self.day, "Life event: " + self.current_event["title"], sector, impact))
            self.news_log = self.news_log[:30]
        elif action == "risky":
            if self.cash < value:
                messagebox.showwarning("Not enough cash", "This choice costs ${:,.2f}. Choose another option.".format(value), parent=win)
                return
            self.cash = round(self.cash - value, 2)
            multiplier = random.choice([0, .25, .6, 1.0, 1.5, 2.2])
            payout = value * multiplier
            self.cash = round(self.cash + payout, 2)
            result = "The venture returned ${:,.2f} on your ${:,.2f} stake (outcome: {:.0f}% return).".format(payout, value, (multiplier - 1) * 100)
        elif action == "skip":
            result = "You passed on the opportunity. No money changed hands."
        else:
            result = "Event resolved."
        self.portfolio_history.append(self.net_worth())
        win.destroy()
        messagebox.showinfo("Event outcome", result)
        if self.screen in ("dashboard", "market", "portfolio", "history", "news", "property", "business", "advanced", "missions"):
            self.dashboard()

    def repay_loan(self):
        # Use integer cents for validation and subtraction to avoid float precision bugs.
        debt_cents = int(round(max(0.0, self.loan) * 100))
        cash_cents = int(round(max(0.0, self.cash) * 100))
        if debt_cents <= 0:
            self.loan = 0.0
            messagebox.showinfo("No debt", "You have no outstanding loans.")
            return
        if cash_cents <= 0:
            messagebox.showwarning("No available cash", "You need available cash before you can repay a loan.")
            return
        max_cents = min(debt_cents, cash_cents)
        amount = simpledialog.askfloat(
            "Repay loan",
            "Outstanding debt: ${:,.2f}\nCash available: ${:,.2f}\nEnter an amount in dollars (e.g. 0.01 for one cent):".format(debt_cents/100, cash_cents/100),
            minvalue=0.01, maxvalue=max_cents/100, parent=self.root)
        if amount is None:
            return
        try:
            amount_cents = int(round(float(amount) * 100))
        except (TypeError, ValueError, OverflowError):
            messagebox.showwarning("Invalid repayment", "Enter a valid amount in dollars.")
            return
        if amount_cents < 1 or amount_cents > max_cents:
            messagebox.showwarning("Invalid repayment", "Enter $0.01 up to ${:,.2f}.".format(max_cents/100))
            return
        self.cash = (cash_cents - amount_cents) / 100
        self.loan = max(0, debt_cents - amount_cents) / 100
        self.portfolio_history.append(self.net_worth())
        messagebox.showinfo("Repayment complete", "Repaid ${:,.2f}. Remaining debt: ${:,.2f}.".format(amount_cents/100, self.loan))
        self.dashboard()

    def topbar(self, title):
        bar = self.frame(self.root, bg=BG); bar.pack(fill="x", padx=22, pady=(16,10))
        left = self.frame(bar, bg=BG); left.pack(side="left")
        self.label(left, "ZERO / TO / HERO", 9, TEAL, True).pack(anchor="w")
        self.label(left, title, 20, TEXT, True).pack(anchor="w", pady=(3,0))
        right = self.frame(bar, bg=BG); right.pack(side="right")
        self.label(right, "DAY %d  •  AGE %d" % (self.day, self.age), 10, MUTED, True).pack(anchor="e")
        self.label(right, self.player_name, 10, TEXT).pack(anchor="e", pady=(4,0))

    def nav(self, active):
        nav = self.frame(self.root, bg=PANEL); nav.pack(fill="x", padx=22, pady=(0,12))
        for key, title, func in [("dashboard","Overview",self.dashboard),("market","Market",self.market),
                                  ("portfolio","Portfolio",self.portfolio),("property","Property",self.property_page),
                                  ("business","Business",self.business_page),("advanced","Funds & bonds",self.advanced_page),
                                  ("missions","Missions",self.missions_page),("history","History",self.history),
                                  ("news","News",self.news_page)]:
            self.button(nav, ("● " if active == key else "") + title, func, active == key,
                        padx=9, pady=8, font=("Segoe UI", 9, "bold")).pack(side="left", padx=2, pady=6)

    def dashboard(self):
        """Main screen redesigned as a compact, interactive stock-market terminal."""
        if self.running and not self.victory_shown and self.net_worth() >= 1_000_000:
            self.victory()
            return
        self.screen = "dashboard"
        self.clear()
        self.topbar("Market terminal")
        self.nav("dashboard")

        outer = self.frame(self.root)
        outer.pack(fill="both", expand=True, padx=20, pady=(0, 14))

        # Live-looking account tiles
        investment_total = (sum(self.holdings[t] * self.stocks[t]["price"] for t in self.stocks)
                            + sum(self.fund_holdings[k] * self.fund_prices[k] for k in self.fund_holdings))
        summary = self.frame(outer)
        summary.pack(fill="x", pady=(0, 10))
        tiles = [
            ("NET WORTH", self.net_worth(), TEAL),
            ("CASH", self.cash, BLUE),
            ("INVESTED", investment_total, GOLD),
            ("DEBT", self.loan + sum(p["mortgage"] for p in self.properties), RED),
        ]
        for title, value, color in tiles:
            tile = self.frame(summary, bg=PANEL, highlightbackground=BORDER, highlightthickness=1)
            tile.pack(side="left", fill="x", expand=True, padx=(0, 7), ipady=3)
            self.label(tile, title, 8, MUTED, True).pack(anchor="w", padx=12, pady=(8, 2))
            self.label(tile, "${:,.2f}".format(value), 15, color, True).pack(anchor="w", padx=12, pady=(0, 8))

        body = self.frame(outer)
        body.pack(fill="both", expand=True)
        left = self.frame(body)
        left.pack(side="left", fill="both", expand=True, padx=(0, 10))
        right = self.panel(body, "Market watch")
        right.pack(side="right", fill="y")

        chart_card = self.panel(left, "Price chart  /  simulated market")
        chart_card.pack(fill="both", expand=True)
        chart_header = self.frame(chart_card, bg=PANEL)
        chart_header.pack(fill="x", padx=14, pady=(0, 4))
        self.chart_ticker = getattr(self, "chart_ticker", "NDM")
        if self.chart_ticker not in self.stocks:
            self.chart_ticker = "NDM"
        stock = self.stocks[self.chart_ticker]
        price = stock["price"]
        history = stock["history"]
        previous = history[-2] if len(history) > 1 else price
        change_pct = ((price / previous) - 1) * 100 if previous else 0
        change_color = GREEN if change_pct >= 0 else RED
        self.label(chart_header, self.chart_ticker, 19, TEXT, True).pack(side="left")
        self.label(chart_header, "${:,.2f}".format(price), 19, TEAL, True).pack(side="left", padx=(12, 8))
        self.label(chart_header, "{:+.2f}% TODAY".format(change_pct), 10, change_color, True).pack(side="left", pady=(4, 0))
        self.label(chart_header, stock["name"] + "  •  " + stock["risk"] + " risk", 9, MUTED).pack(side="right")

        chart = tk.Canvas(chart_card, height=270, bg="#0a1422", highlightthickness=0)
        chart.pack(fill="both", expand=True, padx=12, pady=(0, 10))
        chart.bind("<Configure>", lambda _e, c=chart, t=self.chart_ticker: self.draw_market_chart(c, self.stocks[t]["history"], self.stocks[t]["price"]))
        self.draw_market_chart(chart, history, price)

        controls = self.frame(left)
        controls.pack(fill="x", pady=(8, 0))
        self.button(controls, "BUY THIS STOCK", lambda t=self.chart_ticker: self.quick_buy(t), True).pack(side="left", padx=(0, 7))
        self.button(controls, "REPAY DEBT", self.repay_loan).pack(side="left", padx=(0, 7))
        self.button(controls, "OPEN FULL MARKET", self.market).pack(side="left", padx=(0, 7))
        self.button(controls, "SKIP 5+ DAYS ⏩", self.skip_days, primary=True).pack(side="right", padx=(0, 7))
        self.button(controls, "END DAY →", self.manual_advance).pack(side="right", padx=(0, 7))

        self.label(right, "Tap a ticker to switch the chart", 8, MUTED).pack(anchor="w", padx=13, pady=(0, 7))
        watch = tk.Frame(right, bg=PANEL)
        watch.pack(fill="both", expand=True, padx=8, pady=(0, 8))
        # Show a changing mix of major and high-volatility fictional companies.
        watch_tickers = ["NDM", "CCS", "FFF", "PPG", "VTX", "QEL", "AST", "BWE", "MVH"]
        for ticker in watch_tickers:
            st = self.stocks[ticker]
            hist = st["history"]
            prev = hist[-2] if len(hist) > 1 else st["price"]
            pct = ((st["price"] / prev) - 1) * 100 if prev else 0
            color = GREEN if pct >= 0 else RED
            row = tk.Frame(watch, bg=PANEL2 if ticker == self.chart_ticker else PANEL,
                           highlightbackground=BORDER, highlightthickness=1)
            row.pack(fill="x", pady=2)
            btn = tk.Button(row, text=ticker, command=lambda t=ticker: self.select_chart_stock(t),
                            bg=PANEL2 if ticker == self.chart_ticker else PANEL, fg=TEXT,
                            activebackground=BLUE, activeforeground=TEXT, relief="flat", bd=0,
                            font=("Consolas", 10, "bold"), width=5, cursor="hand2")
            btn.pack(side="left", padx=(4, 2), pady=5)
            tk.Label(row, text="${:.2f}".format(st["price"]), bg=row.cget("bg"), fg=TEXT,
                     font=("Consolas", 9)).pack(side="left", padx=4)
            tk.Label(row, text="{:+.1f}%".format(pct), bg=row.cget("bg"), fg=color,
                     font=("Consolas", 9, "bold")).pack(side="right", padx=7)

        # Briefing strip adds a reason for today's market move.
        if self.last_event:
            headline, sector, impact = self.last_event
        else:
            headline, sector, impact = ("Markets are open", "ALL", 0)
        briefing = self.frame(outer, bg=PANEL, highlightbackground=BORDER, highlightthickness=1)
        briefing.pack(fill="x", pady=(10, 0))
        self.label(briefing, "TODAY'S HEADLINE", 8, GOLD, True).pack(side="left", padx=12, pady=10)
        self.label(briefing, headline, 10, TEXT, True).pack(side="left", padx=8, pady=10)
        self.label(briefing, "{}  •  {:+.1f}% event".format(sector, impact * 100), 9,
                   GREEN if impact >= 0 else RED).pack(side="right", padx=12, pady=10)

        # Reaching $1,000,000 is a milestone, not a modal screen; keep playing.
        self.root.after(1000, self.timer_refresh)

    def select_chart_stock(self, ticker):
        if ticker in self.stocks:
            self.chart_ticker = ticker
            self.dashboard()

    def quick_buy(self, ticker):
        stock = self.stocks[ticker]
        quantity = simpledialog.askfloat("Buy " + ticker,
            "{} costs ${:.2f} per share.\nCash available: ${:,.2f}\nHow many shares would you like to buy?".format(stock["name"], stock["price"], self.cash),
            minvalue=0.0001, parent=self.root)
        if quantity is None:
            return
        cost = quantity * stock["price"]
        if cost > self.cash:
            messagebox.showwarning("Not enough cash", "That order costs ${:,.2f}, but you only have ${:,.2f}.".format(cost, self.cash))
            return
        self.cash = round(self.cash - cost, 2)
        self.holdings[ticker] += quantity
        self.portfolio_history.append(self.net_worth())
        messagebox.showinfo("Order filled", "Bought {:.4f} shares of {} for ${:,.2f}.".format(quantity, ticker, cost))
        self.dashboard()

    def draw_market_chart(self, canvas, values, current_price):
        """Draw a responsive dark trading-terminal chart with grid, area fill and price labels."""
        canvas.delete("all")
        w = max(360, canvas.winfo_width())
        h = max(220, canvas.winfo_height())
        left, right, top, bottom = 58, w - 18, 22, h - 30
        data = list(values[-40:])
        if not data:
            data = [current_price, current_price]
        if len(data) == 1:
            data = [data[0], data[0]]
        lo, hi = min(data), max(data)
        padding = max((hi - lo) * .18, max(1, hi * .015))
        lo, hi = max(0, lo - padding), hi + padding
        span = max(.01, hi - lo)

        # Horizontal grid and axis labels
        for i in range(5):
            y = top + i * (bottom - top) / 4
            value = hi - i * span / 4
            canvas.create_line(left, y, right, y, fill="#203047", dash=(2, 4))
            canvas.create_text(left - 8, y, text="${:,.0f}".format(value), anchor="e",
                               fill="#8fa6c2", font=("Consolas", 8))
        for i, label in enumerate(("40 DAYS AGO", "30D", "20D", "10D", "NOW")):
            x = left + i * (right - left) / 4
            canvas.create_line(x, top, x, bottom, fill="#17263a", dash=(2, 5))
            canvas.create_text(x, h - 12, text=label, anchor="center", fill="#7186a1",
                               font=("Consolas", 7))

        points = []
        for i, value in enumerate(data):
            x = left + i * (right - left) / max(1, len(data) - 1)
            y = bottom - (value - lo) / span * (bottom - top)
            points.extend((x, y))
        # Area under the line gives the chart a trading-app look.
        area = [left, bottom] + points + [right, bottom]
        canvas.create_polygon(*area, fill="#123b43", outline="", smooth=True)
        line_color = GREEN if data[-1] >= data[0] else RED
        canvas.create_line(*points, fill=line_color, width=3, smooth=True, splinesteps=20)
        x_last, y_last = points[-2], points[-1]
        canvas.create_oval(x_last - 4, y_last - 4, x_last + 4, y_last + 4,
                           fill=line_color, outline="#e8fff9", width=1)
        canvas.create_text(right - 2, top - 8, text="SIMULATED PRICE", anchor="ne",
                           fill="#7186a1", font=("Consolas", 8, "bold"))

    def draw_progress(self, parent, fraction):
        c = tk.Canvas(parent, height=12, bg=PANEL, highlightthickness=0)
        c.pack(fill="x", padx=16, pady=10)
        c.create_rectangle(0, 2, 500, 10, fill=PANEL2, outline="")
        c.create_rectangle(0, 2, 500*fraction, 10, fill=TEAL, outline="")

    def timer_refresh(self):
        # Update the countdown label in place. Rebuilding the whole dashboard
        # every second caused flickering and made the interface feel laggy.
        if not self.root.winfo_exists():
            return
        if self.screen not in ("dashboard", "market", "portfolio", "history", "news", "property", "business", "advanced", "missions"):
            return

        if self.running and not self.paused and time.time() - self.last_tick >= self.day_seconds:
            self.advance_day()
            if self.screen == "victory":
                return
            if self.screen == "dashboard":
                self.dashboard()
            elif self.screen == "market":
                self.market()
            elif self.screen == "portfolio":
                self.portfolio()
            elif self.screen == "history":
                self.history()
            elif self.screen == "news":
                self.news_page()
            elif self.screen == "property":
                self.property_page()
            elif self.screen == "business":
                self.business_page()
            elif self.screen == "advanced":
                self.advanced_page()
            elif self.screen == "missions":
                self.missions_page()
            return

        if self.screen == "dashboard" and hasattr(self, "timer_label") and self.timer_label.winfo_exists():
            remaining = self.day_seconds if self.paused else max(0, self.day_seconds - (time.time() - self.last_tick))
            self.timer_label.config(
                text=("PAUSED • " if self.paused else "Next day in  ") +
                     "%02d:%02d" % (int(remaining) // 60, int(remaining) % 60)
            )
        self.root.after(250 if self.screen == "dashboard" else 1000, self.timer_refresh)

    def toggle_pause(self):
        self.paused = not self.paused
        if not self.paused: self.last_tick = time.time()
        self.dashboard()

    def manual_advance(self):
        self.advance_day()
        self.dashboard()

    def market(self):
        self.screen = "market"; self.clear(); self.topbar("Explore the market"); self.nav("market")
        outer = self.frame(self.root); outer.pack(fill="both", expand=True, padx=22, pady=(0,15))
        self.label(outer, "50 fictional companies • Select a stock to inspect its price history and buy shares.", 10, MUTED).pack(anchor="w", pady=(0,10))
        split = self.frame(outer); split.pack(fill="both", expand=True)
        tablebox = self.panel(split, "Available stocks"); tablebox.pack(side="left", fill="both", expand=True, padx=(0,12))
        cols = ("ticker","company","price","trend","risk")
        tree = ttk.Treeview(tablebox, columns=cols, show="headings", height=16)
        for col, label, width in [("ticker","TICKER",70),("company","COMPANY",190),("price","PRICE",90),("trend","TREND",85),("risk","RISK",100)]:
            tree.heading(col,text=label); tree.column(col,width=width,anchor="w")
        tree_scroll = ttk.Scrollbar(tablebox, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=tree_scroll.set)
        tree.pack(side="left", fill="both", expand=True, padx=(10,0), pady=10)
        tree_scroll.pack(side="right", fill="y", padx=(0,10), pady=10)
        for t,s in self.stocks.items():
            tree.insert("", "end", iid=t, values=(t,s["name"],"${:.2f}".format(s["price"]),s["trend"],s["risk"]))
        info = self.panel(split, "Stock details"); info.pack(side="right", fill="y")
        self.label(info, "Choose a company", 15, TEXT, True).pack(anchor="w", padx=16, pady=(8,4))
        self.label(info, "Select a row to view details and trade.", 9, MUTED, wraplength=240).pack(anchor="w", padx=16)
        def selected(_=None):
            sel = tree.selection()
            if not sel: return
            t = sel[0]; self.selected_ticker=t; s=self.stocks[t]
            for w in info.winfo_children(): w.destroy()
            self.label(info, s["name"], 15, TEXT, True, wraplength=240, justify="left").pack(anchor="w", padx=16, pady=(14,4))
            self.label(info, t + "  •  " + s["sector"], 9, MUTED).pack(anchor="w", padx=16)
            self.label(info, "${:.2f}".format(s["price"]), 25, TEAL, True).pack(anchor="w", padx=16, pady=(12,3))
            self.label(info, "Risk: " + s["risk"] + "  •  " + s["trend"], 10, GOLD).pack(anchor="w", padx=16)
            self.draw_stock_chart(info, s["history"][-25:])
            self.label(info, "Shares owned: {:.4f}".format(self.holdings[t]), 10, MUTED).pack(anchor="w", padx=16, pady=5)
            qty = tk.StringVar(value="1")
            self.label(info, "Shares to buy", 9, MUTED, True).pack(anchor="w", padx=16, pady=(10,3))
            ent=tk.Entry(info,textvariable=qty,bg=PANEL2,fg=TEXT,insertbackground=TEXT,relief="flat",font=("Segoe UI",11))
            ent.pack(fill="x", padx=16, ipady=7)
            self.label(info, "Cash available: ${:,.2f}".format(self.cash), 9, MUTED).pack(anchor="w", padx=16, pady=5)
            def buy():
                try: q=float(qty.get())
                except ValueError: messagebox.showerror("Invalid amount","Enter a number of shares."); return
                cost=q*s["price"]
                if q<=0 or cost>self.cash: messagebox.showwarning("Can't buy","Enter a positive amount that fits your available cash."); return
                self.cash=round(self.cash-cost, 2); self.holdings[t]+=q; self.portfolio_history.append(self.net_worth())
                messagebox.showinfo("Order complete","Bought {:.4f} shares of {} for ${:,.2f}.".format(q,t,cost))
                self.market()
            self.button(info,"BUY SHARES",buy,True).pack(fill="x", padx=16, pady=(10,6))
            self.button(info,"VIEW FULL HISTORY",lambda:self.history(t)).pack(fill="x", padx=16, pady=(0,14))
        tree.bind("<<TreeviewSelect>>", selected)
        tree.selection_set(self.selected_ticker)
        selected()

    def draw_stock_chart(self, parent, values):
        c=tk.Canvas(parent,width=250,height=100,bg=PANEL2,highlightthickness=0)
        c.pack(fill="x", padx=14, pady=12)
        if len(values)<2: return
        lo=min(values); hi=max(values); span=max(.01,hi-lo)
        pts=[]
        for i,v in enumerate(values):
            x=8+i*(234/(len(values)-1)); y=86-(v-lo)/span*70
            pts.extend((x,y))
        c.create_line(*pts,fill=TEAL,width=2,smooth=True)
        c.create_text(8,8,anchor="nw",text="RECENT PRICE MOVEMENT",fill=MUTED,font=("Segoe UI",7,"bold"))

    def portfolio(self):
        self.screen="portfolio"; self.clear(); self.topbar("Your portfolio"); self.nav("portfolio")
        outer=self.frame(self.root); outer.pack(fill="both",expand=True,padx=22,pady=(0,15))
        self.label(outer,"Your investments can rise or fall. Selling incurs a fee that depends on the stock's risk.",10,MUTED).pack(anchor="w",pady=(0,10))
        tablebox=self.panel(outer,"Holdings"); tablebox.pack(fill="both",expand=True)
        tree=ttk.Treeview(tablebox,columns=("company","shares","price","value","fee"),show="headings",height=12)
        for col,title,width in [("company","COMPANY",260),("shares","SHARES",140),("price","CURRENT PRICE",140),("value","MARKET VALUE",160),("fee","SELL FEE",110)]:
            tree.heading(col,text=title); tree.column(col,width=width,anchor="w")
        tree.pack(fill="both",expand=True,padx=10,pady=10)
        for t,q in self.holdings.items():
            if q>0:
                s=self.stocks[t]; tree.insert("","end",iid=t,values=(s["name"],"{:.4f}".format(q), "${:.2f}".format(s["price"]), "${:,.2f}".format(q*s["price"]),"{:.1f}%".format(s["fee"]*100)))
        actions=self.frame(outer); actions.pack(fill="x",pady=12)
        self.label(actions,"Cash: ${:,.2f}     Portfolio value: ${:,.2f}".format(self.cash,sum(self.holdings[t]*self.stocks[t]["price"] for t in self.stocks)),12,TEAL,True).pack(side="left")
        def sell():
            sel=tree.selection()
            if not sel: messagebox.showinfo("Choose an investment","Select a holding first."); return
            t=sel[0]; s=self.stocks[t]
            if self.withdrawal_blocked_today:
                messagebox.showwarning("Withdrawal locked","On every tenth day, you cannot sell investments. Keep emergency cash ready."); return
            qty=simpledialog.askfloat("Sell shares","How many shares of {}? You own {:.4f}.".format(t,self.holdings[t]),minvalue=.0001)
            if qty is None:return
            if qty>self.holdings[t]: messagebox.showwarning("Too many shares","You don't own that many.");return
            gross=qty*s["price"]; fee=gross*s["fee"]; proceeds=gross-fee
            self.holdings[t]=max(0.0, self.holdings[t]-qty); self.cash=round(self.cash+proceeds, 2); self.portfolio_history.append(self.net_worth())
            messagebox.showinfo("Sale complete","Sold for ${:,.2f}; fee ${:,.2f}; you received ${:,.2f}.".format(gross,fee,proceeds))
            self.portfolio()
        self.button(actions,"SELL SELECTED (fee applies)",sell,True).pack(side="right")

    def history(self, ticker=None):
        self.screen="history"; self.clear(); self.topbar("Track your progress"); self.nav("history")
        outer=self.frame(self.root); outer.pack(fill="both",expand=True,padx=22,pady=(0,15))
        self.label(outer,"A chart helps you spot patterns. Past performance does not predict future returns.",10,MUTED).pack(anchor="w",pady=(0,10))
        card=self.panel(outer,"Net worth over time"); card.pack(fill="both",expand=True)
        vals=self.portfolio_history[-80:]
        c=tk.Canvas(card,bg=PANEL,width=1000,height=360,highlightthickness=0)
        c.pack(fill="both",expand=True,padx=12,pady=12)
        self.draw_line_chart(c,vals,TEAL)
        self.label(outer,"Current net worth: ${:,.2f}    •    Starting cash: $1,000".format(self.net_worth()),12,TEAL,True).pack(anchor="w",pady=8)
        if ticker and ticker in self.stocks:
            s=self.stocks[ticker]
            self.label(outer,"{} ({}) current price: ${:.2f}".format(s["name"],ticker,s["price"]),10,MUTED).pack(anchor="w")

    def draw_line_chart(self,c,values,color):
        c.delete("all")
        w=max(500,c.winfo_width()); h=max(240,c.winfo_height())
        if len(values)<2: values=[1000,1000]
        lo=min(values); hi=max(values); span=max(1,hi-lo)
        for i in range(5):
            y=30+i*(h-65)/4
            c.create_line(50,y,w-20,y,fill=BORDER)
            val=hi-i*span/4
            c.create_text(42,y,text="${:,.0f}".format(val),anchor="e",fill=MUTED,font=("Segoe UI",8))
        pts=[]
        for i,v in enumerate(values):
            x=55+i*(w-85)/(len(values)-1); y=30+(hi-v)/span*(h-65)
            pts.extend((x,y))
        c.create_line(*pts,fill=color,width=3,smooth=True)
        c.create_text(55,h-15,text="START",anchor="w",fill=MUTED,font=("Segoe UI",8))
        c.create_text(w-20,h-15,text="NOW",anchor="e",fill=MUTED,font=("Segoe UI",8))

    def news_page(self):
        self.screen="news"; self.clear(); self.topbar("News & market events"); self.nav("news")
        outer=self.frame(self.root); outer.pack(fill="both",expand=True,padx=22,pady=(0,15))
        self.label(outer,"Every new day brings a fictional headline that can influence a sector or the whole market.",10,MUTED).pack(anchor="w",pady=(0,10))
        for day,headline,sector,impact in self.news_log[:18]:
            card=self.frame(outer,bg=PANEL,highlightbackground=BORDER,highlightthickness=1)
            card.pack(fill="x",pady=4)
            self.label(card,"DAY %d"%day,9,TEAL,True).pack(side="left",padx=14,pady=13)
            inner=self.frame(card,bg=PANEL);inner.pack(side="left",fill="x",expand=True,pady=10)
            self.label(inner,headline,11,TEXT,True).pack(anchor="w")
            self.label(inner,"Sector: %s  •  Event impact: %+.1f%%"%(sector,impact*100),9,MUTED).pack(anchor="w",pady=(3,0))
        if not self.news_log: self.label(outer,"No headlines yet.",11,MUTED).pack(anchor="w")

    def _page_shell(self, active, title, subtitle):
        self.screen = active
        self.clear()
        self.topbar(title)
        self.nav(active)
        outer = self.frame(self.root)
        outer.pack(fill="both", expand=True, padx=22, pady=(0, 15))
        self.label(outer, subtitle, 10, MUTED, wraplength=1080, justify="left").pack(anchor="w", pady=(0, 10))
        return outer

    def property_page(self):
        outer = self._page_shell("property", "Property portfolio", "Buy fictional properties with a 20% deposit, collect rent every 30 game days, and manage mortgage costs. Property equity counts toward net worth.")
        catalog = [
            ("Studio Apartment", 85000, 520, "Entry-level rental"),
            ("Suburban Townhouse", 240000, 1450, "Higher rent, higher deposit"),
            ("City Duplex", 420000, 2500, "Large cash-flow opportunity"),
            ("Small Retail Unit", 600000, 3300, "Commercial tenant risk")]
        box = self.panel(outer, "Properties for sale"); box.pack(fill="x", pady=(0, 10))
        for name, price, rent, desc in catalog:
            row = self.frame(box, bg=PANEL); row.pack(fill="x", padx=12, pady=6)
            self.label(row, name, 11, TEXT, True).pack(side="left", padx=6)
            self.label(row, "${:,.0f}  •  rent ${:,.0f}/month  •  deposit ${:,.0f}  •  {}".format(price, rent, price*.2, desc), 9, MUTED).pack(side="left", padx=12)
            def buy_property(n=name, v=price, r=rent):
                deposit = round(v * .20, 2)
                if self.cash < deposit:
                    messagebox.showwarning("Deposit too small", "You need ${:,.2f} cash for the 20% deposit.".format(deposit)); return
                if any(p["name"] == n for p in self.properties):
                    messagebox.showinfo("Already owned", "You already own this property."); return
                self.cash = round(self.cash - deposit, 2)
                self.properties.append({"name": n, "value": float(v), "rent": float(r), "mortgage": round(v-deposit, 2), "bought_day": self.day})
                self.portfolio_history.append(self.net_worth())
                self.achievements.add("first_property")
                messagebox.showinfo("Property purchased", "Bought {}. Deposit: ${:,.2f}; mortgage: ${:,.2f}. Rent and costs settle every 30 days.".format(n, deposit, v-deposit))
                self.property_page()
            self.button(row, "BUY", buy_property, primary=True, padx=10, pady=5).pack(side="right", padx=4)
        owned = self.panel(outer, "Owned properties"); owned.pack(fill="both", expand=True)
        if not self.properties:
            self.label(owned, "No properties yet. Save a deposit or grow your income first.", 10, MUTED).pack(anchor="w", padx=15, pady=14)
        for p in self.properties:
            equity = p["value"] - p["mortgage"]
            row = self.frame(owned, bg=PANEL); row.pack(fill="x", padx=12, pady=5)
            self.label(row, "{}  |  value ${:,.0f}  |  mortgage ${:,.2f}  |  equity ${:,.2f}  |  rent ${:,.0f}/month".format(p["name"], p["value"], p["mortgage"], equity, p["rent"]), 9, TEXT).pack(side="left", padx=3)
            self.button(row, "SELL", lambda prop=p: self.sell_property(prop), padx=9, pady=5).pack(side="right", padx=3)

    def sell_property(self, prop):
        if prop not in self.properties:
            return
        gross = round(prop["value"] * .97, 2)  # simulated 3% selling costs
        proceeds = round(gross - prop["mortgage"], 2)
        self.cash = round(self.cash + proceeds, 2)
        self.properties.remove(prop)
        self.portfolio_history.append(self.net_worth())
        messagebox.showinfo("Property sold", "Sold for ${:,.2f} before mortgage payoff. After 3% costs and ${:,.2f} mortgage repayment, cash changed by ${:,.2f}.".format(gross, prop["mortgage"], proceeds))
        self.property_page()

    def business_page(self):
        outer = self._page_shell("business", "Businesses & side hustles", "Side hustles refresh every 2–3 game days. Businesses pay out every 10 game days. All income is simulated.")
        hustles = [("Mow a lawn", 100, 2), ("Tutor a student", 140, 3), ("Deliver groceries", 85, 2), ("Freelance design job", 260, 3)]
        box = self.panel(outer, "Side hustles"); box.pack(fill="x", pady=(0, 10))
        for name, payout, cooldown in hustles:
            row = self.frame(box, bg=PANEL); row.pack(fill="x", padx=12, pady=5)
            last = self.side_hustle_day.get(name, -999)
            available = self.day - last >= cooldown
            self.label(row, "{}  •  ${:,.0f} payout  •  {}".format(name, payout, "Available" if available else "Available in {} day(s)".format(cooldown-(self.day-last))), 10, TEXT, True).pack(side="left", padx=5)
            def do_hustle(n=name, pay=payout, cd=cooldown):
                last_day = self.side_hustle_day.get(n, -999)
                if self.day-last_day < cd:
                    messagebox.showinfo("Not ready", "This job needs a little time before you can do it again."); return
                bonus = random.choice([0, 0, 0, 25, 50])
                self.cash = round(self.cash + pay + bonus, 2)
                self.side_hustle_day[n] = self.day
                self.achievements.add("first_hustle")
                self.portfolio_history.append(self.net_worth())
                messagebox.showinfo("Hustle complete", "Earned ${:,.2f}{}".format(pay+bonus, " including a ${} bonus".format(bonus) if bonus else ""))
                self.business_page()
            self.button(row, "WORK", do_hustle, primary=available, padx=10, pady=5).pack(side="right", padx=4)
        offers = [("Online Store", 2500, 160, "A small online retail operation"), ("Lawn Care Crew", 6500, 380, "Equipment and repeat customers"), ("Coffee Kiosk", 18000, 950, "More income, higher overhead"), ("Software Startup", 45000, 2200, "High potential, high risk")]
        shop = self.panel(outer, "Businesses to acquire"); shop.pack(fill="x", pady=(0, 10))
        for name, price, income, desc in offers:
            row = self.frame(shop, bg=PANEL); row.pack(fill="x", padx=12, pady=5)
            self.label(row, "{}  •  ${:,.0f}  •  ${:,.0f} per 10-day payout  •  {}".format(name, price, income, desc), 9, TEXT, True).pack(side="left", padx=5)
            def buy_biz(n=name, cost=price, inc=income):
                if self.cash < cost:
                    messagebox.showwarning("Not enough cash", "You need ${:,.2f} cash to buy this business.".format(cost)); return
                if any(b["name"] == n for b in self.businesses):
                    messagebox.showinfo("Already owned", "You already own this business."); return
                self.cash = round(self.cash-cost, 2)
                self.businesses.append({"name": n, "value": float(cost), "income": float(inc), "level": 1})
                self.achievements.add("first_business")
                self.portfolio_history.append(self.net_worth())
                messagebox.showinfo("Business acquired", "You bought {}. Simulated income arrives every 10 game days.".format(n))
                self.business_page()
            self.button(row, "BUY", buy_biz, primary=True, padx=10, pady=5).pack(side="right", padx=4)
        owned = self.panel(outer, "Your businesses"); owned.pack(fill="both", expand=True)
        if not self.businesses:
            self.label(owned, "No businesses owned yet.", 10, MUTED).pack(anchor="w", padx=15, pady=12)
        for b in self.businesses:
            row = self.frame(owned, bg=PANEL); row.pack(fill="x", padx=12, pady=5)
            self.label(row, "{}  •  value ${:,.0f}  •  ${:,.0f} per 10-day payout  •  level {}".format(b["name"], b["value"], b["income"], b["level"]), 10, TEXT).pack(side="left", padx=4)
            upgrade_cost = 1000 * b["level"]
            self.button(row, "UPGRADE (${:,.0f})".format(upgrade_cost), lambda biz=b: self.upgrade_business(biz), padx=9, pady=5).pack(side="right", padx=3)
            self.button(row, "SELL", lambda biz=b: self.sell_business(biz), padx=9, pady=5).pack(side="right", padx=3)

    def sell_business(self, biz):
        if biz not in self.businesses:
            return
        proceeds = round(biz["value"] * .90, 2)
        self.cash = round(self.cash + proceeds, 2)
        self.businesses.remove(biz)
        self.portfolio_history.append(self.net_worth())
        messagebox.showinfo("Business sold", "Sold {} for ${:,.2f} after estimated selling costs.".format(biz["name"], proceeds))
        self.business_page()

    def upgrade_business(self, biz):
        upgrade_cost = 1000 * biz["level"]
        if self.cash < upgrade_cost:
            messagebox.showwarning("Not enough cash", "This upgrade costs ${:,.0f}.".format(upgrade_cost)); return
        self.cash = round(self.cash-upgrade_cost, 2)
        biz["level"] += 1
        # Gentle compounding: each upgrade boosts income by 12% and value by 8%,
        # instead of the old 50% income / 35% value jumps.
        biz["income"] = round(biz["income"] * 1.12, 2)
        biz["value"] = round(biz["value"] * 1.08, 2)
        self.portfolio_history.append(self.net_worth())
        messagebox.showinfo("Upgrade complete", "{} is now level {}.".format(biz["name"], biz["level"]))
        self.business_page()

    def advanced_page(self):
        outer = self._page_shell("advanced", "Funds, bonds & alternative assets", "Diversify beyond individual shares. These are fictional instruments with simplified simulated returns, not real investment advice.")
        items = [("GROW", "Broad Market Index Fund", "Diversified, medium risk"), ("BOND", "Government Bond Fund", "Lower volatility, slower growth"), ("GOLD", "Gold Tracker", "Can swing when markets are nervous")]
        box = self.panel(outer, "Available investments"); box.pack(fill="x", pady=(0, 10))
        for code, name, desc in items:
            row = self.frame(box, bg=PANEL); row.pack(fill="x", padx=12, pady=7)
            self.label(row, "{} ({})  •  ${:.2f}  •  {}  •  units owned: {:.4f}".format(name, code, self.fund_prices[code], desc, self.fund_holdings[code]), 10, TEXT, True).pack(side="left", padx=5)
            def buy_fund(c=code):
                amount = simpledialog.askfloat("Buy investment", "How many dollars to invest in {}?\nAvailable cash: ${:,.2f}".format(c, self.cash), minvalue=.01, maxvalue=max(.01, self.cash), parent=self.root)
                if amount is None: return
                cents = int(round(amount*100)); cashc = int(round(self.cash*100))
                if cents < 1 or cents > cashc:
                    messagebox.showwarning("Invalid amount", "The amount must fit your cash balance."); return
                cost = cents/100
                self.cash = round(self.cash-cost, 2)
                self.fund_holdings[c] += cost/self.fund_prices[c]
                self.achievements.add("first_fund")
                self.portfolio_history.append(self.net_worth())
                self.advanced_page()
            def sell_fund(c=code):
                units = self.fund_holdings[c]
                if units <= 0:
                    messagebox.showinfo("No units", "You do not own this investment yet."); return
                amount = simpledialog.askfloat("Sell investment", "Units to sell (you own {:.4f}):".format(units), minvalue=.0001, maxvalue=units, parent=self.root)
                if amount is None: return
                if amount <= 0 or amount > units + 1e-9: return
                proceeds = round(amount*self.fund_prices[c]*.995, 2)
                self.fund_holdings[c] = max(0.0, units-amount)
                self.cash = round(self.cash+proceeds, 2)
                self.portfolio_history.append(self.net_worth())
                self.advanced_page()
            self.button(row, "BUY", buy_fund, primary=True, padx=10, pady=5).pack(side="right", padx=3)
            self.button(row, "SELL", sell_fund, padx=10, pady=5).pack(side="right", padx=3)
        total = sum(self.fund_holdings[k]*self.fund_prices[k] for k in self.fund_holdings)
        self.label(outer, "Alternative investment value: ${:,.2f}  •  cash: ${:,.2f}".format(total, self.cash), 12, TEAL, True).pack(anchor="w", pady=10)
        history = self.panel(outer, "Your fund units"); history.pack(fill="both", expand=True)
        for code, name, _ in items:
            self.label(history, "{}: {:.4f} units × ${:.2f} = ${:,.2f}".format(name, self.fund_holdings[code], self.fund_prices[code], self.fund_holdings[code]*self.fund_prices[code]), 10, MUTED).pack(anchor="w", padx=15, pady=5)

    def missions_page(self):
        outer = self._page_shell("missions", "Missions & achievements", "Complete optional objectives to earn rewards and track your progress. Rewards are one-time; your net worth includes cash, stocks, funds, property equity and business value, minus debt.")
        missions = [
            ("cash_2500", "Build a $2,500 cash reserve", lambda: self.cash >= 2500, 250),
            ("stock_1000", "Hold at least $1,000 in stocks", lambda: sum(self.holdings[t]*self.stocks[t]["price"] for t in self.stocks) >= 1000, 300),
            ("first_property", "Buy your first property", lambda: any(True for _ in self.properties), 500),
            ("first_business", "Own your first business", lambda: any(True for _ in self.businesses), 350),
            ("first_fund", "Invest in a fund or bonds", lambda: any(v > 0 for v in self.fund_holdings.values()), 150),
            ("net_10000", "Reach $10,000 net worth", lambda: self.net_worth() >= 10000, 500),
            ("net_100000", "Reach $100,000 net worth", lambda: self.net_worth() >= 100000, 2500),
        ]
        box = self.panel(outer, "Missions"); box.pack(fill="both", expand=True, pady=(0, 10))
        for key, title, condition, reward in missions:
            done = bool(condition())
            row = self.frame(box, bg=PANEL); row.pack(fill="x", padx=12, pady=6)
            status = "COMPLETED" if done else "IN PROGRESS"
            self.label(row, ("✓ " if done else "○ ")+title+"  •  Reward: ${:,.0f}  •  {}".format(reward, status), 10, GREEN if done else TEXT, True).pack(side="left", padx=5)
            if done and key not in self.claimed_missions:
                self.button(row, "CLAIM", lambda k=key, r=reward: self.claim_mission(k, r), primary=True, padx=10, pady=5).pack(side="right", padx=4)
            elif key in self.claimed_missions:
                self.label(row, "CLAIMED", 8, MUTED, True).pack(side="right", padx=8)
        ach = self.panel(outer, "Achievement badges"); ach.pack(fill="x")
        badges = [("first_hustle", "First paycheck"), ("first_property", "Property owner"), ("first_business", "Entrepreneur"), ("first_fund", "Diversified investor")]
        for key, label in badges:
            self.label(ach, ("🏆 " if key in self.achievements else "○ ")+label, 10, GOLD if key in self.achievements else MUTED).pack(anchor="w", padx=15, pady=4)
        self.label(outer, "Current net worth: ${:,.2f}  •  Age: {}  •  Day: {}".format(self.net_worth(), self.age, self.day), 11, TEAL, True).pack(anchor="w", pady=10)

    def claim_mission(self, key, reward):
        if key in self.claimed_missions:
            return
        self.cash = round(self.cash + reward, 2)
        self.claimed_missions.add(key)
        self.portfolio_history.append(self.net_worth())
        messagebox.showinfo("Mission reward", "Mission complete! ${:,.2f} added to cash.".format(reward))
        self.missions_page()

    def victory(self):
        """Show the $1,000,000 completion screen once per game."""
        if self.victory_shown:
            return
        self.victory_shown = True
        self.running = False
        self.paused = False
        self._save_stock_history()
        self.screen = "victory"
        self.clear()

        outer = self.frame()
        outer.pack(fill="both", expand=True, padx=60, pady=45)
        self.label(outer, "ZERO / TO / HERO", 11, TEAL, True).pack(anchor="w", pady=(10, 35))
        self.label(outer, "YOU DID IT!", 38, GOLD, True).pack(anchor="w", pady=(15, 8))
        self.label(outer, "You reached millionaire status.", 19, TEXT, True).pack(anchor="w")
        self.label(
            outer,
            "Your net worth is ${:,.2f}.".format(self.net_worth()),
            17, TEAL, True
        ).pack(anchor="w", pady=(14, 8))
        self.label(
            outer,
            "You reached the $1,000,000 goal on day {} at age {}.\n"
            "You can keep building your fictional portfolio or return to the main menu.".format(self.day, self.age),
            11, MUTED, justify="left", wraplength=760
        ).pack(anchor="w", pady=(0, 28))

        actions = self.frame(outer)
        actions.pack(anchor="w")
        self.button(actions, "CONTINUE PLAYING  →", self.continue_after_victory, True).pack(side="left", padx=(0, 10))
        self.button(actions, "RETURN TO MENU", self.show_menu).pack(side="left")

    def continue_after_victory(self):
        """Resume play without showing the completion screen again this game."""
        self.running = True
        self.paused = False
        self.last_tick = time.time()
        self.dashboard()

    def skip_days(self):
        """Advance at least five game days without opening a stack of event popups."""
        days = simpledialog.askinteger(
            "Skip days",
            "How many game days would you like to skip? Enter 5 or more.",
            initialvalue=5, minvalue=5, maxvalue=3650, parent=self.root)
        if days is None:
            return
        self.paused = True
        days_advanced = 0
        for _ in range(days):
            self.advance_day(show_event=False)
            days_advanced += 1
            if self.screen == "victory":
                break
        if self.screen == "victory":
            return
        self.paused = False
        self.last_tick = time.time()
        self.portfolio_history.append(self.net_worth())
        messagebox.showinfo("Time skipped", "Advanced {} days. You are now on day {} (age {}).".format(days_advanced, self.day, self.age))
        self.dashboard()

if __name__ == "__main__":
    root = tk.Tk()
    app = ZeroToHero(root)
    root.mainloop()
