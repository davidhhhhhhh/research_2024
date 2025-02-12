from StudentSimulator.ideaToText import Decision

class OffsetExtra(Decision):
    def registerChoices(self):
        self.addChoice('codeStructure', {
            '''import acm.graphics.*;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.File;
import java.text.SimpleDateFormat;
import java.util.Date;
import javax.imageio.ImageIO;

public class DrawStructure{{
    private static final int INNER_CANVAS_WIDTH = 600;
    private static final int INNER_CANVAS_HEIGHT = 400;
    private static final int OUTER_CANVAS_WIDTH = 800;
    private static final int OUTER_CANVAS_HEIGHT = 600;

    public static void main(String[] args) {{
        // Create an off-screen GCanvas
        GCanvas canvas = new GCanvas();
        canvas.setSize(OUTER_CANVAS_WIDTH, OUTER_CANVAS_HEIGHT);

        // Initialize structure parameters
        {InitializeStructureParametersPyramidOffset}

        // Optionally add centering assist lines
        {AddCenteringAssistLines}

        // Draw a pyramid
        for (int i = 0; i < BRICKS_IN_BASE; i++) {{
            // Calculate row variables
            int nBricks = BRICKS_IN_BASE - i;
            int rowWidth = nBricks * BRICK_WIDTH;
            double rowY = OFFSET_Y + 500 - (i + 1) * BRICK_HEIGHT;
            double rowX = OFFSET_X + (800 - rowWidth) / 2.0;

            // Draw a single row
            for (int j = 0; j < nBricks; j++) {{
                // Add a single brick
                double x = rowX + j * BRICK_WIDTH;
                GRect brick = new GRect(x, rowY, BRICK_WIDTH, BRICK_HEIGHT);

                // Determine if the brick is filled
                {SetBrickFilled}

                brick.setColor({BrickColorPyramidExtra});
                canvas.add(brick);
            }}
        }}
        // Draw the inner canvas boundary
        GRect innerCanvasBoundary = new GRect((OUTER_CANVAS_WIDTH - INNER_CANVAS_WIDTH) / 2,
                                               (OUTER_CANVAS_HEIGHT - INNER_CANVAS_HEIGHT) / 2,
                                               INNER_CANVAS_WIDTH, INNER_CANVAS_HEIGHT);
        innerCanvasBoundary.setColor(Color.BLACK);
        canvas.add(innerCanvasBoundary);
        
        // Save the canvas as an image
        saveCanvasAsImage(canvas);
    }}
    private static void saveCanvasAsImage(GCanvas canvas) {{
                    BufferedImage image = new BufferedImage(OUTER_CANVAS_WIDTH, OUTER_CANVAS_HEIGHT, BufferedImage.TYPE_INT_RGB);
                    Graphics g = image.getGraphics();
                    g.setColor(Color.WHITE);
                    g.fillRect(0, 0, OUTER_CANVAS_WIDTH, OUTER_CANVAS_HEIGHT);
    
                    // Draw the current canvas content to the buffered image
                    canvas.paint(g);
    
                    // Generate a unique filename using a timestamp
                    String timestamp = new SimpleDateFormat("yyyyMMddHHmmss").format(new Date());
                    String filename = "offset_extra_" + timestamp + ".png";
    
                    try {{
                        // Write the buffered image to a file
                        ImageIO.write(image, "png", new File(filename));
                        System.out.println("Image saved as " + filename);
                    }} catch (Exception e) {{
                        e.printStackTrace();
                    }}
                }}            
            }}''': 1
        })

    def render(self):
        return self.getChoice('codeStructure')


class InitializeStructureParametersPyramidOffset(Decision):
    def registerChoices(self):
        self.addChoice('bricksInBase', {
            '14': 5,
            '13': 4,
            '12': 3,
            '11': 2,
            '10': 1
        })
        self.addChoice('brickWidth', {
            '30': 10,
            '40': 1
        })
        self.addChoice('brickHeight', {
            '10': 10,
            '20': 1
        })
        self.addChoice('OFFSET_Y', {
            '-20': 1,
            '10': 1,
            '20': 1,
            '-30': 1
        })
        self.addChoice('OFFSET_X', {
            '20': 1,
            '40': 1
        })

    def render(self):
        bricksInBase = int(self.getChoice('bricksInBase'))
        brickWidth = self.getChoice('brickWidth')
        brickHeight = self.getChoice('brickHeight')
        OFFSET_X = self.getChoice('OFFSET_X')
        OFFSET_Y = self.getChoice('OFFSET_Y')

        return '\n'.join([
            'int BRICKS_IN_BASE = {};'.format(bricksInBase),
            'int BRICK_WIDTH = {};'.format(brickWidth),
            'int BRICK_HEIGHT = {};'.format(brickHeight),
            'int OFFSET_X = {};'.format(OFFSET_X),
            'int OFFSET_Y = {};'.format(OFFSET_Y)
        ])


class BrickColorPyramidExtra(Decision):
    def registerChoices(self):
        self.addChoice('brickColor', {
            'Color.GRAY': 1,
            'Color.BLUE': 1,
            'Color.GREEN': 1,
            'Color.RED': 1,
            'Color.ORANGE': 1,
            'Color.YELLOW': 1
        })

    def render(self):
        return self.getChoice('brickColor')
