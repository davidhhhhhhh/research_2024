import acm.graphics.*;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.File;
import java.text.SimpleDateFormat;
import java.util.Date;
import javax.imageio.ImageIO;

public class DrawStructure251{
    private static final int INNER_CANVAS_WIDTH = 600;
    private static final int INNER_CANVAS_HEIGHT = 400;
    private static final int OUTER_CANVAS_WIDTH = 800;
    private static final int OUTER_CANVAS_HEIGHT = 600;

    public static void main(String[] args) {
        // Create an off-screen GCanvas
        GCanvas canvas = new GCanvas();
        canvas.setSize(OUTER_CANVAS_WIDTH, OUTER_CANVAS_HEIGHT);

        // Initialize structure parameters
        int BRICKS_IN_BASE = 14;
int BRICK_WIDTH = 40;
int BRICK_HEIGHT = 20;
int OFFSET_X = 20;
int OFFSET_Y = -20;

        // Optionally add centering assist lines
        canvas.add(new GLine(0, canvas.getHeight() / 2, canvas.getWidth(), canvas.getHeight() / 2));

        // Draw a pyramid
        for (int i = 0; i < BRICKS_IN_BASE; i++) {
            // Calculate row variables
            int nBricks = BRICKS_IN_BASE - i;
            int rowWidth = nBricks * BRICK_WIDTH;
            double rowY = OFFSET_Y + 500 - (i + 1) * BRICK_HEIGHT;
            double rowX = OFFSET_X + (800 - rowWidth) / 2.0;

            // Draw a single row
            for (int j = 0; j < nBricks; j++) {
                // Add a single brick
                double x = rowX + j * BRICK_WIDTH;
                GRect brick = new GRect(x, rowY, BRICK_WIDTH, BRICK_HEIGHT);

                // Determine if the brick is filled
                brick.setFilled(true);

                brick.setColor(Color.MAGENTA);
                canvas.add(brick);
            }
        }
        // Save the canvas as an image
        saveCanvasAsImage(canvas);
    }
    private static void saveCanvasAsImage(GCanvas canvas) {
                    BufferedImage image = new BufferedImage(OUTER_CANVAS_WIDTH, OUTER_CANVAS_HEIGHT, BufferedImage.TYPE_INT_RGB);
                    Graphics g = image.getGraphics();
                    g.setColor(Color.WHITE);
                    g.fillRect(0, 0, OUTER_CANVAS_WIDTH, OUTER_CANVAS_HEIGHT);
    
                    // Draw the current canvas content to the buffered image
                    canvas.paint(g);
    
                    // Generate a unique filename using a timestamp
                    String timestamp = new SimpleDateFormat("yyyyMMddHHmmss").format(new Date());
                    String filename = "offset_extra_" + timestamp + ".png";
    
                    try {
                        // Write the buffered image to a file
                        ImageIO.write(image, "png", new File(filename));
                        System.out.println("Image saved as " + filename);
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                }            
            }