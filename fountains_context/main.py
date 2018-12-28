try:
    from OpenGL.GL import *
    from OpenGL.GLUT import *
except:
    print "OpenGL wrapper for python not found"

from context import Context


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
