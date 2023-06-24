import random
import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
hands = mp_hands.Hands()
# Define the list of picture coordinates
picture_coordinates = [(100, 100), (200, 200), (300, 300), (400, 400), (500, 500)]
picture_coordinates
points = 0

# Randomly select initial coordinates for each picture
random.shuffle(picture_coordinates)

# take the window size
window_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
x1 = int(window_size[0]/2) - 100
y1 = int(window_size[1]/2) - 50
x2 = int(window_size[0]/2) + 100
y2 = int(window_size[1]/2) + 50


text = 'Rectangle Game'
text_size= cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)

touching_rectangle = False
touching = False

x1_black = 300
y1_black = 100
x2_black = 500
y2_black = 200

start_game = False


# All the coordinates related to the snake Game
# Game constants
WINDOW_WIDTH = window_size[0]
WINDOW_HEIGHT = window_size[1]
SNAKE_SIZE = 20
FOOD_SIZE = 20

snake_x_player1 = [WINDOW_WIDTH // 4]
snake_y_player1 = [WINDOW_HEIGHT // 2]
food_x = random.randint(0, WINDOW_WIDTH - FOOD_SIZE)
food_y = random.randint(0, WINDOW_HEIGHT - FOOD_SIZE)

# Initialize player 2 snake and food positions
snake_x_player2 = [3 * WINDOW_WIDTH // 4]
snake_y_player2 = [WINDOW_HEIGHT // 2]

score_player1 = 0
score_player2 = 0
snake_game = False





while True:
    success, image = cap.read()

    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # Here the image arrray is read only mode
    image.flags.writeable = False
    results = hands.process(image)
    # print(results)
    # Here the image arrray is writeable mode
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            

            # Check if index finger is touching any picture
            index_finger_coordinates = (
                hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image.shape[1],
                hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image.shape[0]
            )
            thumb_coordinates = (
                hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * image.shape[1],
                hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * image.shape[0]
            )
            if abs(index_finger_coordinates[0] - thumb_coordinates[0]) < 15 and abs(index_finger_coordinates[1] - thumb_coordinates[1]) < 15:
            # print(np.sqrt((index_finger_coordinates[0] - thumb_coordinates[0])**2 + (index_finger_coordinates[1] - thumb_coordinates[1])**2))
            # if np.sqrt((index_finger_coordinates[0] - thumb_coordinates[0])**2 + (index_finger_coordinates[1] - thumb_coordinates[1])**2) < 15:
                if start_game == False:
                    if abs(x1 - index_finger_coordinates[0]+ 100) < 100 and abs(y1 - index_finger_coordinates[1]+50) < 50 :
                        
                        print("Touching the rectangle")
                        touching_rectangle = True
                        start_game = True
                    
                    elif abs(x1 - index_finger_coordinates[0]+ 100) < 100 and abs(100 - index_finger_coordinates[1]+50) < 50 :
                        print('This is awesome')
                        snake_game = True
                        
                
                
                elif abs(x1_black - index_finger_coordinates[0]+100) < 100 and abs(y1_black - index_finger_coordinates[1]+50) < 50:
                    touching = True

                for i, (x,y) in enumerate(picture_coordinates):
                    if abs(x - index_finger_coordinates[0]) < 30 and abs(y - index_finger_coordinates[1]) < 30:
                    
                    # Index finger is touching the picture
                        picture_coordinates.pop(i)
                        picture_coordinates.append((random.randint(0, window_size[0]), random.randint(0, window_size[1])))
                        points += 1
                        break
            
            else:
                touching = False
                
                num_hands = len(results.multi_hand_landmarks)
        if num_hands >= 2 and snake_game:
            player1_landmarks = results.multi_hand_landmarks[0]
            player2_landmarks = results.multi_hand_landmarks[1]
            
                        # Player 1 - Get index finger tip coordinates
            index_finger_x_player1 = int(player1_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * WINDOW_WIDTH)
            index_finger_y_player1 = int(player1_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * WINDOW_HEIGHT)

            # Player 2 - Get index finger tip coordinates
            index_finger_x_player2 = int(player2_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * WINDOW_WIDTH)
            index_finger_y_player2 = int(player2_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * WINDOW_HEIGHT)

            # Player 1 - Move snake based on index finger direction
            if len(snake_x_player1) > 1:
                dx = snake_x_player1[-1] - snake_x_player1[-2]
                dy = snake_y_player1[-1] - snake_y_player1[-2]
                
                # asari ni lekna mildo raixa
                # if abs(dx) > abs(dy):
                #     index_finger_x_player1 += SNAKE_SIZE if dx > 0 else -SNAKE_SIZE
                # else:
                #     index_finger_y_player1 += SNAKE_SIZE if dy > 0 else -SNAKE_SIZE
                
                if abs(dx) > abs(dy):
                # If dx > 0, it means the movement is towards the right
                    if dx > 0:
                        index_finger_x_player1 += SNAKE_SIZE
                    else:
                        index_finger_x_player1 -= SNAKE_SIZE
                else:
                    # If dy > 0, it means the movement is downwards
                    if dy > 0:
                        index_finger_y_player1 += SNAKE_SIZE
                    else:
                        index_finger_y_player1 -= SNAKE_SIZE


                    

            # Player 2 - Move snake based on index finger direction
            if len(snake_x_player2) > 1:
                dx = snake_x_player2[-1] - snake_x_player2[-2]
                dy = snake_y_player2[-1] - snake_y_player2[-2]

                if abs(dx) > abs(dy):
                    index_finger_x_player2 += SNAKE_SIZE if dx > 0 else -SNAKE_SIZE
                else:
                    index_finger_y_player2 += SNAKE_SIZE if dy > 0 else -SNAKE_SIZE

            # Player 1 - Check collision with food
            if abs(snake_x_player1[-1] - food_x) < SNAKE_SIZE and abs(snake_y_player1[-1] - food_y) < SNAKE_SIZE:
                snake_x_player1.append(food_x)
                snake_y_player1.append(food_y)
                food_x = random.randint(0, WINDOW_WIDTH - FOOD_SIZE)
                food_y = random.randint(0, WINDOW_HEIGHT - FOOD_SIZE)
                score_player1 += 1

            # Player 2 - Check collision with food
            if abs(snake_x_player2[-1] - food_x) < SNAKE_SIZE and abs(snake_y_player2[-1] - food_y) < SNAKE_SIZE:
                snake_x_player2.append(food_x)
                snake_y_player2.append(food_y)
                food_x = random.randint(0, WINDOW_WIDTH - FOOD_SIZE)
                food_y = random.randint(0, WINDOW_HEIGHT - FOOD_SIZE)
                score_player2 += 1

            # Player 1 - Move snake
            snake_x_player1.append(index_finger_x_player1)
            snake_y_player1.append(index_finger_y_player1)

            # Player 2 - Move snake
            snake_x_player2.append(index_finger_x_player2)
            snake_y_player2.append(index_finger_y_player2)


            # Comment out the Remove tail segment to make writting place.
            # # Player 1 - Remove tail segment
            if len(snake_x_player1) > 1:
                snake_x_player1.pop(0)
                snake_y_player1.pop(0)

            # Player 2 - Remove tail segment
            if len(snake_x_player2) > 1:
                snake_x_player2.pop(0)
                snake_y_player2.pop(0)

            # Player 1 - Check collision with boundaries
            if (
                snake_x_player1[-1] < 0 or
                snake_x_player1[-1] >= WINDOW_WIDTH or
                snake_y_player1[-1] < 0 or
                snake_y_player1[-1] >= WINDOW_HEIGHT
            ):
                # Game over for player 1
                cv2.putText(image, "Game Over - Player 1", (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                snake_x_player1 = [WINDOW_WIDTH // 4]
                snake_y_player1 = [WINDOW_HEIGHT // 2]
                score_player1 = 0

            # Player 2 - Check collision with boundaries
            if (
                snake_x_player2[-1] < 0 or
                snake_x_player2[-1] >= WINDOW_WIDTH or
                snake_y_player2[-1] < 0 or
                snake_y_player2[-1] >= WINDOW_HEIGHT
            ):
                # Game over for player 2
                cv2.putText(image, "Game Over - Player 2", (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                snake_x_player2 = [3 * WINDOW_WIDTH // 4]
                snake_y_player2 = [WINDOW_HEIGHT // 2]
                score_player2 = 0

            # Draw player 1 snake
            for x, y in zip(snake_x_player1, snake_y_player1):
                cv2.rectangle(image, (x, y), (x + SNAKE_SIZE, y + SNAKE_SIZE), (0, 255, 0), cv2.FILLED)

            # Draw player 2 snake
            for x, y in zip(snake_x_player2, snake_y_player2):
                cv2.rectangle(image, (x, y), (x + SNAKE_SIZE, y + SNAKE_SIZE), (255, 0, 0), cv2.FILLED)

            # Draw food
            cv2.rectangle(image, (food_x, food_y), (food_x + FOOD_SIZE, food_y + FOOD_SIZE), (0, 0, 255), cv2.FILLED)

    if snake_game:
        # Draw scores
        cv2.putText(image, f"Player 1 Score: {score_player1}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(image, f"Player 2 Score: {score_player2}", (WINDOW_WIDTH - 300, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

            
    if touching and snake_game == False:
            # Calculate the new position of the black box based on the index finger's movement
            x1_black = int(index_finger_coordinates[0]) - 100
            y1_black = int(index_finger_coordinates[1]) - 50
            x2_black = int(index_finger_coordinates[0]) + 100
            y2_black = int(index_finger_coordinates[1]) + 50
                
    if touching_rectangle and snake_game == False:
        

        cv2.rectangle(image, (x1_black, y1_black), (x2_black, y2_black), (0,0,0), cv2.FILLED)
        
        
        for x, y in picture_coordinates:
           
            cv2.rectangle(image, (x-30, y-30), (x+30, y+30), (0, 255, 0), cv2.FILLED)
        cv2.putText(image, f"Points: {points}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        
    elif touching_rectangle==False and snake_game==False:
        # Only draw the rectangle if touching_rectangle is False
        cv2.rectangle(image, (x1, y1), (x2, y2), (105, 136, 207), cv2.FILLED) 
        cv2.putText(image, f"Start Rectangle Game", (x1+10, y1+50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
        
        cv2.rectangle(image, (x1, 50), (x2, 150), (105, 136, 207), cv2.FILLED) 
        cv2.putText(image, f"Start Snake Game", (x1+10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)





        # Display the points counter
    cv2.imshow("Games", image)
    if cv2.waitKey(5) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
