import pygame 
from pygame.locals import * 
from OpenGL.GL import * 
from OpenGL.GLU import * 
pygame.init() 
pygame.display.set_mode((800, 600), DOUBLEBUF|OPENGL) 
Point1=((2.4)(3,7))
Point2=((6,8),(4,8))

def Point1():
    glBegin(GL_LINE) 
    for edge in Point2:
        for vertex in edge:
            glVertex3fv(Point1[vertex]) 
    
    glEnd()
glVertex3fv((1, 1, 1)) 
glVertex3fv((1, 1, -1)) 

def main(): 
    pygame.init()
display = (800, 600) 
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)