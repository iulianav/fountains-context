try:
    from OpenGL.GL import (
        GL_COLOR_BUFFER_BIT,
        GL_MODELVIEW,
        GL_POINT_SMOOTH,
        GL_PROJECTION,
        glClear,
        glClearColor,
        glEnable,
        glLoadIdentity,
        glMatrixMode,
        glViewport,
    )
    from OpenGL.GLU import (
        gluLookAt,
        gluPerspective,
    )
    from OpenGL.GLUT import (
        GLUT_DOUBLE,
        glutCreateWindow,
        glutDisplayFunc,
        glutInit,
        glutInitDisplayMode,
        glutInitWindowPosition,
        glutInitWindowSize,
        glutMainLoop,
        glutPostRedisplay,
        glutReshapeFunc,
        glutSwapBuffers,
    )
except:
    print "OpenGL wrapper for python not found"

from fountain import Fountain
from particle import Particle
from utils import gaussianDistance


class Context:

    def __init__(
        self, mass=0.009, gravity=-9.83, fountains_nr=5,
        ):

        self.fountains = []
        self.fountains_nr = fountains_nr
        self.gravity = gravity
        self.mass = mass

        for i in range(self.fountains_nr):
            self.fountains.append(Fountain(self))

    def reshape(self, width, height):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60, width / height, 1.0, 10000.0)
        glMatrixMode(GL_MODELVIEW)

    def display(self):
        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();
        gluLookAt(0.0, 240.0, 1000.0,
                  0.0, 240.0, 0.0,
                  0.0, 1.0, 0.0);
        glClear(GL_COLOR_BUFFER_BIT)

        for i in self.fountains:
            i.life -= 1
            i.init()
            i.update()

        glutPostRedisplay()
        glutSwapBuffers()

def main():
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_DOUBLE)

    glutInitWindowSize(800, 600)

    glutInitWindowPosition(100, 100)

    glutCreateWindow('Particle System')

    fountains = Context()

    glutDisplayFunc(fountains.display)

    glutReshapeFunc(fountains.reshape)

    glEnable(GL_POINT_SMOOTH);

    glutMainLoop()

if __name__ == '__main__':
    main()
