from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

class MainScene(VoiceoverScene):
    def construct(self):
        # ----------------------------------------------------------------------
        # SET UP AZURE SERVICE FOR VOICEOVER
        # ----------------------------------------------------------------------
        self.set_speech_service(
            AzureService(
                subscription_key="FRr7HXnUnGXaZC9M9V0atRglReaD9MrHBywSDwSIcZcZKNohilGIJQQJ99BBACYeBjFXJ3w3AAAYACOG4O5a",
                region="eastus"
            )
        )
        
        # ----------------------------------------------------------------------
        # INTRODUCTION: Title Display in TOP ZONE
        # ----------------------------------------------------------------------
        title = Text("Introduction to Eigenvalues and Eigenvectors", font_size=40)
        title.to_edge(UP, buff=0.5)  # TOP zone
        
        with self.voiceover(text="Welcome to our short introduction on eigenvalues and eigenvectors. In this lesson, we will learn what eigenvalues and eigenvectors are and why they are important in linear algebra.") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        
        # Pause to let viewers digest the title
        self.wait(0.5)
        
        # ----------------------------------------------------------------------
        # DISPLAY THE MATRIX AND ITS ROLE (CENTER ZONE)
        # ----------------------------------------------------------------------
        # Create a 2x2 matrix for demonstration
        matrix_elements = [["2", "1"], ["1", "2"]]
        matrix = Matrix(matrix_elements, element_to_mobject_config={"font_size": 36})
        matrix.move_to(ORIGIN)  # CENTER zone
        
        # Group the matrix with its label
        # Using MathTex instead of Tex avoids LaTeX compilation issues
        matrix_label = MathTex(r"A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}", font_size=36)
        matrix_label.next_to(matrix, DOWN, buff=0.5)
        matrix_group = VGroup(matrix, matrix_label)
        
        with self.voiceover(text="Here we have a simple matrix. To find its eigenvalues we subtract a scalar times the identity matrix and set the determinant to zero.") as tracker:
            self.play(Create(matrix_group), run_time=tracker.duration)
        
        # ----------------------------------------------------------------------
        # STEP-BY-STEP: Finding the Eigenvalues (LEFT ZONE)
        # ----------------------------------------------------------------------
        # Explanation text on eigenvalue equation
        eigen_eq = MathTex(r"\det\Bigl(\begin{pmatrix} 2-\lambda & 1 \\ 1 & 2-\lambda \end{pmatrix}\Bigr)=0", font_size=36)
        eigen_eq.to_edge(LEFT, buff=0.5)  # LEFT zone
        
        with self.voiceover(text="To find the eigenvalues, we need to solve the equation where the determinant of the matrix after subtracting lambda times the identity is zero. In this case, you compute the determinant of the matrix with entries two minus lambda, one, one, and two minus lambda.") as tracker:
            self.play(Write(eigen_eq), run_time=tracker.duration)
        
        # Highlight the eigenvalue result
        eigen_values = MathTex(r"\lambda=1 \quad\text{or}\quad \lambda=3", font_size=36)
        eigen_values.next_to(eigen_eq, DOWN, buff=0.5)
        
        with self.voiceover(text="When you solve this equation, you find that the eigenvalues are one and three. This means that the matrix stretches its eigenvectors by these respective factors.") as tracker:
            self.play(Write(eigen_values), run_time=tracker.duration)
        
        # ----------------------------------------------------------------------
        # DEMONSTRATE EIGENVECTORS (RIGHT ZONE)
        # ----------------------------------------------------------------------
        # Create a simple arrow to represent an eigenvector
        eigenvector_arrow = Arrow(start=ORIGIN, end=RIGHT * 2, buff=0, color=YELLOW)
        # Position the eigenvector group in the RIGHT zone
        eigenvector_text = Text("Eigenvector", font_size=24)
        eigenvector_text.next_to(eigenvector_arrow, RIGHT, buff=0.5)
        eigenvector_group = VGroup(eigenvector_arrow, eigenvector_text)
        eigenvector_group.to_edge(RIGHT, buff=0.5)  
        
        with self.voiceover(text="An eigenvector is a special vector that only gets scaled during the transformation. Notice how it maintains its direction even as it is stretched by the matrix.") as tracker:
            self.play(Create(eigenvector_group), run_time=tracker.duration)
        
        # ----------------------------------------------------------------------
        # SUMMARY SLIDE TO REINFORCE KEY POINTS
        # ----------------------------------------------------------------------
        summary_title = Text("Summary", font_size=40)
        summary_title.to_edge(UP, buff=0.5)
        
        summary_points = VGroup(
            Tex(r"\bullet\ Eigenvalues are the scaling factors.", font_size=36),
            Tex(r"\bullet\ Eigenvectors retain their direction.", font_size=36),
            Tex(r"\bullet\ They are fundamental in linear algebra and applications.", font_size=36)
        )
        summary_points.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        summary_points.to_edge(LEFT, buff=0.5)
        
        with self.voiceover(text="In summary, eigenvalues tell us how much an eigenvector is stretched, and the eigenvectors themselves maintain their direction. These concepts are crucial in many applications across science and engineering.") as tracker:
            # Remove earlier elements using explicit fade out
            self.play(
                FadeOut(matrix_group),
                FadeOut(eigen_eq),
                FadeOut(eigen_values),
                FadeOut(eigenvector_group),
                run_time=tracker.duration * 0.3
            )
            self.play(Write(summary_title), run_time=tracker.duration * 0.3)
            self.play(Write(summary_points), run_time=tracker.duration * 0.5)
            self.wait(tracker.duration * 0.2)
        
        # Final fadeout of summary elements
        self.play(FadeOut(summary_title), FadeOut(summary_points), run_time=tracker.duration * 0.2)
        
        # End scene pause
        self.wait(1)
