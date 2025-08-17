from manim import *

INDIGO = "#392864"
STEAM_BLUE = "#0E4780"

class Logos(Scene):
    def construct(self):
        # Set background color to white
        self.camera.background_color = WHITE 

        # Load and scale logos (force them to be once color so they show on white bg)
        # All logos must be in the "images" directory relative to this script as well as svg files
        m1 = SVGMobject("images/steam-logo.svg").scale(0.7).set_color(STEAM_BLUE)
        m2 = SVGMobject("images/minecraft-seeklogo.svg").scale(0.85)
        m3 = SVGMobject("images/roblox.svg").scale(0.5).set_color(INDIGO)
        m4 = SVGMobject("images/Fortnite.svg").scale(1.3).set_color(BLACK)

        # Put logos in a vertical group, spaced evenly
        logos = VGroup(m1, m2, m3, m4).arrange(DOWN, buff=0.5).scale(0.8).to_edge(UP)

        # Add text below the logos (black text for contrast)
        t = Text("Dash_Ketch Gaming").set_color(BLACK).next_to(logos, DOWN)

        # Play animations (sequential writing)
        self.play(Write(m1, run_time=1.5))
        self.play(Write(m2, run_time=1.5))
        self.play(Write(m3, run_time=1.5))
        self.play(Write(m4, run_time=1.5))
        self.play(Write(t, run_time=2))

        self.wait(2)
