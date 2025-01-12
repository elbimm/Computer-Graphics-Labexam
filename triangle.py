import pygame
from pygame.locals import *
from OpenGL.GL import *

def draw_triangle():
    """
    Function to draw a triangle using OpenGL.
    """
    glBegin(GL_TRIANGLES)  # Start specifying a triangle primitive
    glColor3f(0.5, 0.0, 0.5)  # Set color to purple
    glVertex2f(-0.5, -0.5)  # Specify the first vertex of the triangle
    glVertex2f(0.5, -0.5)  # Specify the second vertex of the triangle
    glVertex2f(0.0, 0.5)  # Specify the third vertex of the triangle
    glEnd()  # End the triangle primitive

def main():
    pygame.init()

    
    screen_width = 800
    screen_height = 600
    pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)


    glViewport(0, 0, screen_width, screen_height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1, 1, -1, 1, -1, 1)  # Set up a simple orthographic projection

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw the triangle
        draw_triangle()

        # Swap the buffers to display the frame
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
