try:
    from OpenGL.GL import GL_POINT_SMOOTH, GL_POINTS, glEnable
    from OpenGL.GLUT import (
        sys,
        GLUT_DOUBLE,
        glutCreateWindow,
        glutDisplayFunc,
        glutInit,
        glutInitDisplayMode,
        glutInitWindowPosition,
        glutInitWindowSize,
        glutMainLoop,
        glutReshapeFunc,
    )
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
