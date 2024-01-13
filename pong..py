import pygame
import sys

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#display
width, height = 1000, 1200
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Case Design")
#frame info
frame_width, frame_height = 500, 800
frame_color = BLACK
frame_rect = pygame.Rect((width - frame_width) // 2, (height - frame_height) // 2, frame_width, frame_height)

#tilted shelves
shelf_width = 100
shelf_color = BLACK
shelf_rects = [
    pygame.Rect((width - shelf_width) // 2, i * (frame_height // 4) + (height - frame_height) // 2, shelf_width, 10) 
    for i in range(1, 5)
]

#shelves
for i, shelf_rect in enumerate(shelf_rects):
    tilt_amount = i * 20  # Adjust the tilt amount as needed
    shelf_rect.x += tilt_amount

# Draw the doors
door_width, door_height = 50, 100
door_color = BLACK
left_door_rect = pygame.Rect((width - shelf_width) // 2 - door_width, (height - frame_height) // 2 + frame_height // 4 - door_height // 2, door_width, door_height)
right_door_rect = pygame.Rect((width + shelf_width) // 2, (height - frame_height) // 2 + frame_height // 4 - door_height // 2, door_width, door_height)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(WHITE)

    # Draw the frame
    pygame.draw.rect(screen, frame_color, frame_rect)

    # Draw the tilted shelves
    for shelf_rect in shelf_rects:
        pygame.draw.rect(screen, shelf_color, shelf_rect)

    # Draw the doors
    pygame.draw.rect(screen, door_color, left_door_rect)
    pygame.draw.rect(screen, door_color, right_door_rect)

    # Update the display
    pygame.display.flip()
