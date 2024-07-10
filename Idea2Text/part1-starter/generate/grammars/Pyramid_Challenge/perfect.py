from ideaToText import Decision

class Perfect(Decision):
    def registerChoices(self):
        self.addChoice('codeStructure', {
            '''import acm.graphics.*;
import acm.program.*;
import java.awt.Color;

public class DrawPyramidStructure extends GraphicsProgram {{
    public void run() {{
        // Set canvas size
        {SetCanvasSizePyramid}

        // Initialize structure parameters
        {InitializeStructureParametersPyramid}

        // Draw a pyramid
        for (int i = 0; i < BRICKS_IN_BASE; i++) {{
            // Calculate row variables
            int nBricks = BRICKS_IN_BASE - i;
            int rowWidth = nBricks * BRICK_WIDTH;
            double rowY = getHeight() - (i + 1) * BRICK_HEIGHT;
            double rowX = (getWidth() - rowWidth) / 2.0;

            // Draw a single row
            for (int j = 0; j < nBricks; j++) {{
                // Add a single brick
                double x = rowX + j * BRICK_WIDTH;
                GRect brick = new GRect(x, rowY, BRICK_WIDTH, BRICK_HEIGHT);

                // Determine if the brick is filled
                {SetBrickFilled}

                add(brick);
            }}
        }}
    }}

    public static void main(String[] args) {{
        // Start the GraphicsProgram
        new DrawPyramidStructure().start(args);
    }}
}}''': 1
        })

    def render(self):
        return self.getChoice('codeStructure')


class SetCanvasSizePyramid(Decision):
    def registerChoices(self):
        self.addChoice('canvasWidth', {
            '600': 1
        })
        self.addChoice('canvasHeight', {
            '400': 1
        })

    def render(self):
        return 'setSize({}, {});'.format(self.getChoice('canvasWidth'), self.getChoice('canvasHeight'))


class InitializeStructureParametersPyramid(Decision):
    def registerChoices(self):
        self.addChoice('bricksInBase', {
            '14': 5,
            '13': 4,
            '12': 3,
            '11': 2,
            '10': 1
        })
        self.addChoice('brickWidth', {
            '40': 4,
            '80': 1
        })
        self.addChoice('brickHeight', {
            '20': 4,
            '40': 1
        })

    def render(self):
        bricksInBase = int(self.getChoice('bricksInBase'))
        brickWidth = self.getChoice('brickWidth')
        brickHeight = self.getChoice('brickHeight')

        return '\n'.join([
            'int BRICKS_IN_BASE = {};'.format(bricksInBase),
            'int BRICK_WIDTH = {};'.format(brickWidth),
            'int BRICK_HEIGHT = {};'.format(brickHeight)
        ])
