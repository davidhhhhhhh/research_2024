from ideaToText import Decision

class SingleRow(Decision):
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
    private static final int CANVAS_WIDTH = 600;
    private static final int CANVAS_HEIGHT = 400;
    private static final int IMAGE_WIDTH = 800;
    private static final int IMAGE_HEIGHT = 600;

    public static void main(String[] args) {{
        // Create an off-screen GCanvas
        GCanvas canvas = new GCanvas();
        canvas.setSize(CANVAS_WIDTH, CANVAS_HEIGHT);

        // Initialize starting position and other parameters
        {InitializeBrickParametersSingleRow}

        // Draw bricks
        for (int i = 0; i < NUM_BRICKS; i++) {{
            int x = i * (BRICK_WIDTH + BRICK_SEP);
            int y = START_Y - BRICK_HEIGHT / 2;
            GRect brick = new GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT);

            // Add a rogue brick condition
            if (i == ROGUE_BRICK_INDEX) {{
                brick.setFilled(true);
                brick.setColor(Color.RED);
            }} else {{
                brick.setColor({BrickColorSingleRow});
            }}

            canvas.add(brick);
        }}
    // Save the canvas as an image
        saveCanvasAsImage(canvas);
    }}
    private static void saveCanvasAsImage(GCanvas canvas) {{
        BufferedImage image = new BufferedImage(IMAGE_WIDTH, IMAGE_HEIGHT, BufferedImage.TYPE_INT_RGB);
        Graphics g = image.getGraphics();
        g.setColor(Color.WHITE);
        g.fillRect(0, 0, IMAGE_WIDTH, IMAGE_HEIGHT);

        // Draw the current canvas content to the buffered image
        BufferedImage canvasImage = new BufferedImage(CANVAS_WIDTH, CANVAS_HEIGHT, BufferedImage.TYPE_INT_RGB);
        Graphics canvasGraphics = canvasImage.getGraphics();
        canvasGraphics.setColor(Color.WHITE);
        canvasGraphics.fillRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
        canvas.paint(canvasGraphics);

        // Center the canvas on the image
        int offsetX = (IMAGE_WIDTH - CANVAS_WIDTH) / 2;
        int offsetY = (IMAGE_HEIGHT - CANVAS_HEIGHT) / 2;
        g.drawImage(canvasImage, offsetX, offsetY, null);

        // Draw a border around the canvas area
        g.setColor(Color.BLACK);
        g.drawRect(offsetX, offsetY, CANVAS_WIDTH, CANVAS_HEIGHT);

        // Generate a unique filename using a timestamp
        String timestamp = new SimpleDateFormat("yyyyMMddHHmmss").format(new Date());
        String filename = "singleRow_" + timestamp + ".png";

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


class SetCanvasSizeSingleRow(Decision):
    def registerChoices(self):
        self.addChoice('canvasWidth', {
            '400': 2,
            '600': 1
        })
        self.addChoice('canvasHeight', {
            '260': 3,
            '200': 1,
            '300': 1
        })

    def render(self):
        return 'setSize({}, {});'.format(self.getChoice('canvasWidth'), self.getChoice('canvasHeight'))


class InitializeBrickParametersSingleRow(Decision):
    def registerChoices(self):
        self.addChoice('numBricks', {
            'int NUM_BRICKS = 3;': 2,
            'int NUM_BRICKS = 4;': 1,
            'int NUM_BRICKS = 5;': 1,
            'int NUM_BRICKS = 6;': 1
        })
        self.addChoice('brickWidth', {
            '40': 2,
            '30': 1,
            '20': 1
        })
        self.addChoice('brickHeight', {
            '20': 2,
            '30': 1,
            '40': 1
        })
        self.addChoice('brickSeparation', {
            'int BRICK_SEP = 5;': 1,
            'int BRICK_SEP = 0;': 3,
            'int BRICK_SEP = 10;': 1
        })
        self.addChoice('rogueBrickIndex', {
            'int ROGUE_BRICK_INDEX = -1;': 3,  # No rogue brick
            'int ROGUE_BRICK_INDEX = 1;': 1,  # Rogue brick at position 1
            'int ROGUE_BRICK_INDEX = 2;': 1  # Rogue brick at position 2
        })
        self.addChoice('startYPosition', {
            'int START_Y = canvas.getHeight() - 20;': 3,  # High probability to start at the bottom
            'int START_Y = canvas.getHeight() / 2;': 1,
            'int START_Y = 40;': 1,
            'int START_Y = -40;': 1
        })

    def render(self):
        return '\n'.join([
            self.getChoice('numBricks'),
            'int BRICK_WIDTH = {};'.format(self.getChoice('brickWidth')),
            'int BRICK_HEIGHT = {};'.format(self.getChoice('brickHeight')),
            self.getChoice('brickSeparation'),
            self.getChoice('rogueBrickIndex'),
            self.getChoice('startYPosition')
        ])


class BrickColorSingleRow(Decision):
    def registerChoices(self):
        self.addChoice('brickColor', {
            'Color.GRAY': 2,
            'Color.BLUE': 1,
            'Color.GREEN': 1,
            'Color.YELLOW': 1,
            'Color.ORANGE': 1,
            'Color.MAGENTA': 1
        })

    def render(self):
        return self.getChoice('brickColor')