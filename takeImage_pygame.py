import pygame

import cv2

pygame.init()

# --- create PyGame image ---

pg_img = pygame.Surface((400, 200))
pygame.draw.circle(pg_img, (255,0,0), (0,0), 200)

# --- display PyGame image ---

screen = pygame.display.set_mode((400, 400))

screen.fill((255,255,255))
screen.blit(pg_img, pg_img.get_rect())
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            running = False

pygame.quit()
color_image = pygame.surfarray.array3d(pg_img)
print(color_image.shape)

#pygame use (image_with,image_height, channels)
#but openCv use (image_height,image_weight, channels)
#for this we have to use cv2 transpoze
#for change with,height to height with
color_image = cv2.transpose(color_image)
print(color_image.shape)

color_image = cv2.cvtColor(color_image, cv2.COLOR_RGB2BGR)

#show the image
#cv2.imshow('color',color_image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# some changing  on image

# rotate is Rotation of an image for an angle \theta is achieved by the transformation matrix
#color_image = cv2.rotate(color_image, cv2.ROTATE_90_CLOCKWISE)

#if we didn't used transpoze we cant use BGR2GRAY

gray_image = cv2.cvtColor(color_image,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()











