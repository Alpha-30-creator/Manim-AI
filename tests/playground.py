"""Playground script for testing anything.
"""
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

class Main(ThreeDScene, VoiceoverScene):
    def construct(self):
        # Set up the Azure speech service
        self.set_speech_service(
            AzureService(
                subscription_key="FRr7HXnUnGXaZC9M9V0atRglReaD9MrHBywSDwSIcZcZKNohilGIJQQJ99BBACYeBjFXJ3w3AAAYACOG4O5a",
                region="eastus"
            )
        )
        
        # Create initial 2D scene elements
        title = Text("Dimension Transitions", font_size=40)
        title.to_edge(UP)
        
        circle = Circle(radius=2, color=BLUE)
        
        # First voiceover: Introduce and show title
        with self.voiceover(text="Welcome to this demonstration of transitioning between 2D and 3D scenes in Manim.") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        
        # Second voiceover: Show circle
        with self.voiceover(text="Let's start with a simple 2D circle.") as tracker:
            self.play(Create(circle), run_time=tracker.duration)
        
        # Save the original camera state
        original_phi = self.camera.phi
        original_theta = self.camera.theta
        
        # Third voiceover: Transition to 3D
        with self.voiceover(text="Now, watch as we transition into the third dimension.") as tracker:
            # Remove 2D elements before transitioning to 3D
            self.play(
                FadeOut(title),
                FadeOut(circle),
                run_time=tracker.duration * 0.3
            )
            
            # Set up 3D scene
            axes = ThreeDAxes()
            sphere = Surface(
                lambda u, v: np.array([
                    1.5 * np.cos(u) * np.cos(v),
                    1.5 * np.cos(u) * np.sin(v),
                    1.5 * np.sin(u)
                ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2]
            )
            sphere.set_fill(BLUE_E, opacity=0.7)
            
            # Move to 3D perspective
            self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
            self.play(
                Create(axes),
                Create(sphere),
                run_time=tracker.duration * 0.7
            )
        
        # Fourth voiceover: Rotate the 3D scene
        with self.voiceover(text="This three-dimensional sphere demonstrates proper perspective handling in Manim.") as tracker:
            self.begin_ambient_camera_rotation(rate=0.2)
            self.wait(tracker.duration * 0.8)
            self.stop_ambient_camera_rotation()
        
        # Fifth voiceover: Transition back to 2D
        with self.voiceover(text="Now, let's return to two dimensions.") as tracker:
            # Remove 3D objects
            self.play(
                FadeOut(axes),
                FadeOut(sphere),
                run_time=tracker.duration * 0.4
            )
            
            # Reset camera to original orientation
            self.set_camera_orientation(
                phi=original_phi,
                theta=original_theta
            )
            
            # Create new 2D elements
            new_title = Text("Back to 2D", font_size=40)
            new_title.to_edge(UP)
            square = Square(side_length=4, color=RED)
            
            # Introduce new 2D elements
            self.play(
                Write(new_title),
                run_time=tracker.duration * 0.3
            )
            self.play(
                Create(square),
                run_time=tracker.duration * 0.3
            )
        
        # Add explanation text
        explanation = Text("Smooth transitions between dimensions", font_size=24)
        explanation.next_to(new_title, DOWN, buff=0.5)
        
        # Final voiceover
        with self.voiceover(
            text="By carefully managing camera orientation and element transitions, we can achieve smooth transitions between 2D and 3D scenes.",
            subcaption="Clean Transitions are Key!"
        ) as tracker:
            self.play(
                Write(explanation),
                run_time=tracker.duration * 0.5
            )
            self.wait(tracker.duration * 0.3)
            # Clean up all elements at the end
            self.play(
                FadeOut(new_title),
                FadeOut(explanation),
                FadeOut(square),
                run_time=tracker.duration * 0.2
            )
