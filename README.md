# Snake-B-Snake

## Demo
Demo Video: https://youtu.be/XUuJWbDor0k

## Github Repositiory
Github Repo: https://github.com/LuisaLara18/Snake-B-Snake

## Description
Enjoy the world-famous _Snake_ game with an added twist! Instead of just eating apples to grow, you can eat **multiple** types of fruits to grow in different increments of length.
Watch out! Beware of the many trash piles randomized throughout the screen. If you eat one by accident, you'll shrink in size! You can either shrink by one block or all the way to twenty blocks!

### How to Play:
Just like Google's _Snake_, you use your up, down, left, and right keyboard keys to control the movement of your snake. The goal is to grow your snake as long as possible by using the fruits to grow! However, with each fruit's randomized position, be weary of how you collect them. You can collect a fruit, grow a large increment, and immediately catapult into one of the trash piles, into yourself, or the edge of the screen, creating an instant death.

### Snake-B-Snake Logistics:
Each file within the Snake-B-Snake repository works to show the brainstorming and mechanics of the game! The proposal.md file showed the initial idea of Snake-B-Snake, the README.md file explains the final product of the game, the requirements.txt file lists the Python libraries utilized, and the src folder contains the project Python file and game graphics. The apple, banana, blueberries, dragonfruit, trash pile, and snake graphics were all created by me in Adobe Photoshop using a pixel art style. 

In the game, each fruit is only spawned once and changes position whenever your snake collides with it. Depending on the type of fruit, it can grow either one block in length or all the way to ten blocks.

- Eating an apple grows your snake by one block.
- Eating a banana grows your snake by three blocks.
- Eating a blueberry grows your snake by five blocks.
- Eating a dragonfruit grows your snake by ten blocks.
The multiple trash piles also follow the same philosophy, except you can either shrink between one block to twenty blocks in length.

- Three trash piles remove one block from your snake.
- Two trash piles remove five blocks from your snake.
- Two trash piles remove ten blocks from your snake.
- One trash pile removes twenty blocks from your snake.
There is no way to differentiate between with trash pile eliminates what amount of block, so it's a gamble every time you collide with one!

There are several ways to die in the game. The main one is eating the trash piles, but you can accidentally hit the screens edge or run into yourself. You can also die by consuming some of the fruits, as when you consume the larger increment ones, you can lose control of where you are and run into yourself, the screen edge, or a trash pile. Lesson learned, watch the way you collect the fruits to avoid an accidental death! 

Depending on the way to die, you can either restart the game or the game program will close on it's own. If the snake loses length by consuming too many trash piles, then the game program will close by itself. However, if you crash into yourself or the screen edge, you are able to restart the game without the program closing.

### What did I do Differently:
Although I used a video tutorial to help me create a simplier version of Google's _Snake_ game, I implemented different functions to make my game unique. After learning how to program the snake to grow one block in length, I was able to create multiple methods under the Snake class that allowed different increments of lengths to be gained depending on the fruit consumed. I also learned how to remove different increments of length by creating different methods using the pop() method. 

Different customization tactics I did from the video was the scoreboard and visuals. For the scoreboards, instead of having it count the number of apples or fruits collected, I programmed it to count the block length of the snake. For the visuals, I created them all through Photoshop instead of getting them from Google.

### Future Areas of Improvement:
There were some features I wished I was able to code for this project. I wished I was able to implement a despawning feature if the trash piles or fruits weren't collected in time, but I didn't implement it due to the probability of the game being too frustrating have a fruit move spaces after trying to reach for it. My proposal.md file also contained the idea that the blueberries, dragonfruit, and banana would customize your snake, but I thought it wouldn't have made the game more interesting and would have lacked a fun game play mechanic.

Hopefully in the future I am able to gain the skills I need to implement a despawn and customization mechanic in the future, but I am happy with how my game turned out to be.

With all being said, I hope you have fun growing your snake in _Snake-B-Snake_!

## Video Inspiration Credits
https://www.youtube.com/watch?v=QFvqStqPCRU
