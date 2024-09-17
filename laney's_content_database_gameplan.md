# Laney's Content Database Gameplan

## Goal (Task & Purpose)

The goal of this project is to create a comprehensive content database for my client, Laney. We're organizing all her long-form blog posts and related short-form social posts in one place.

This database treats long-form posts (like newsletters and blog posts) as "hub" content, with short-form content (like Instagram posts) as "spokes" extending from the hub.

At the end of the day, this setup is designed to help us easily track, repurpose, and create content across different platforms (while keeping everything organized in one unified structure).

## Components (Pieces & Functions)

### Database Properties

The database uses specific properties — which I essentially think of like variables. These properties define the content and the relationships between hub content (blog posts) and spoke content (social posts). I've outlined the relevant properties for you below, including instructions on how to handle each one.

#### 1. Item

**Definition:**
The unique identifier for each entry in the database.

**Instructions:**

- Use a decimal system (e.g., 1, 1.1, 2, 2.1).
- Blog posts use whole numbers.
- Instagram posts use .1 decimal (e.g., 1.1 for the Instagram post related to blog post 1).

#### 2. Post Title

**Definition:**  
The title or headline of the post (regardless of whether it's long-form or short-form content).

**Instructions:**  

- For main posts (long-form content), use the exact title or headline from the blog post's file name, excluding the "FCD_{number}" suffix and the file extension.
- For social posts (spokes), prepend the corresponding hub post's title with "[Instagram Post]" to distinguish it from the original long-form post's title.

#### 3. Subtitle / Description

**Definition:**  
The subtitle or brief description of the content.

**Instructions:**  

- Include this when available from the blog post content.
- If no subtitle exists, but there's a relevant excerpt or short description that fits, use that.
- Don't force-fit this — only fill this property out if it makes sense to.

#### 4. Content Type

**Definition:**  
This defines the type of content. It's a select property with the following options:  
`Newsletter`, `Blog Post`, `Podcast`, `Video`, `Instagram Post`, `Facebook Post`, `Tweet`, `Twitter Thread`, `LinkedIn Post`, `Email`, `Email Sequence`, `Landing Page`, `Sales Page`, `Course Module`.

**Instructions:**  

- Choose the appropriate content type(s) from the list.
- Multiple types can be used, separated by commas (e.g., "Blog Post, Newsletter").

#### 5. Status

**Definition:**  
A select property with four options: `Upcoming`, `Unknown`, `In progress`, and `Published`.

**Instructions:**  

- `Upcoming`: Use for posts that are planned but not created yet.
- `Unknown`: Use for social posts (spokes) that have a corresponding main post (hub) which has already been published, and this social post's "status" property is still blank.
- `In progress`: For content that Laney and I are actively working on.
- `Published`: For content that's completed and live.

#### 6. Main Topic

**Definition:**  
The primary topic(s) of the post.

**Instructions:**  

- Choose one main topic whenever possible.
- If needed for more context and specificity, you can include up to 2-3 topics, separated by commas.

#### 7. Subtopics

**Definition:**  
Relevant supporting topics that provide more context or depth to the main topic.

**Instructions:**  

- Choose between 3-5 subtopics.
- Separate subtopics with commas instead of semicolons.
- Keep this list tight and on-point, unless more comprehensive context is needed.

#### 8. Action Date

**Definition:**  
The date I ghostwrote (or will ghostwrite) the post.

**Instructions:**  

- Leave this field blank unless I've already specified the action date.

#### 9. Publish Date

**Definition:**  
The date when the post was (or will be) published.

**Instructions:**  

- Leave blank unless a publish date is already provided.

#### 10. Published Link

**Definition:**  
The URL of the published blog post.

**Instructions:**  

- Extract this URL from the markdown-formatted link found at the end of the blog post content (usually labeled with CTA text like "Read On Blog").
- Paste the link into this property.

#### 11. Related Resources

**Definition:**  
A field for any links or resources related to the post.

**Instructions:**  

- Include Notion links when available.
- Leave this blank unless I've already included the resources.

#### 12. Main Post (Hub)

**Definition:**  
A relation property linking a social post (spoke) to its corresponding main post (hub).

**Instructions:**  

- If you're working with a main post (hub) item, leave this blank (because it is the main post).
- If you're working with a social post (spoke) item, copy and paste the main post's "Post Title" here. (I'll fill in the Notion link later.)

#### 13. Social Posts (Spokes)

**Definition:**  
A relation property linking a main post (hub) to its corresponding social posts (spokes).

**Instructions:**  

- If you're working with a social post (spoke) item, leave this blank (because it is the spoke).
- If you're working with a main post (hub) item, copy and paste the social post's "Post Title" here. (I'll fill in the Notion link later.)

#### 14. Instagram Caption

**Definition:**  
The caption for the Instagram post.

**Instructions:**  

- Include the full caption text when available.
- If not available, leave this blank for now.

#### 15. First Created

**Definition:**  
The date and time when the database item was first created.

**Instructions:**  

- Use the specific date and time format: "Month DD, YYYY HH:MM AM/PM" (e.g., "September 14, 2024 10:06 AM").
- Leave this field blank unless it's already filled in.

#### 16. Last Edited

**Definition:**  
The date and time when the database item was last edited.

**Instructions:**  

- Use the specific date and time format: "Month DD, YYYY HH:MM AM/PM" (e.g., "September 14, 2024 10:06 AM").
- Leave this blank unless it's already populated.

### Examples

```csv
Item,Post Title,Subtitle / Description,Content Type,Status,Main Topic,Subtopics,Action Date,Publish Date,Published Link,Related Resources,Main Post (Hub),Social Posts (Spokes),Instagram Caption,First Created,Last Edited
1,3 Little-Known Benefits Of Buying A Toddler Dog (4 Months & Older) vs A Puppy (4 Months & Younger),,"Blog Post, Newsletter",Published,"Puppies, Toddler Dogs",,"August 2, 2024","August 3, 2024",https://www.fineanddandyaussiedoodles.com/post/3-little-known-benefits-of-buying-a-toddler-dog-4-months-older-vs-a-puppy-4-months-younger,Laney Content Call 01 – Interview Questions (https://www.notion.so/Laney-Content-Call-01-Interview-Questions-459baada40774e05b8693a638d24df92?pvs=21) ,,[Instagram Post] 3 Little-Known Benefits Of Buying A Toddler Dog (4 Months & Older) vs A Puppy (4 Months & Younger) (https://www.notion.so/Instagram-Post-3-Little-Known-Benefits-Of-Buying-A-Toddler-Dog-4-Months-Older-vs-A-Puppy-4-Mon-31526b83c3b643ac96f214eb71bb4eff?pvs=21),,"August 28, 2024 11:19 AM","September 14, 2024 10:06 AM"
1.1,[Instagram Post] 3 Little-Known Benefits Of Buying A Toddler Dog (4 Months & Older) vs A Puppy (4 Months & Younger),,Instagram Post,Upcoming,"Puppies, Toddler Dogs",,,,,,3 Little-Known Benefits Of Buying A Toddler Dog (4 Months & Older) vs A Puppy (4 Months & Younger) (https://www.notion.so/3-Little-Known-Benefits-Of-Buying-A-Toddler-Dog-4-Months-Older-vs-A-Puppy-4-Months-Younger-922de65aefc241549ae8e6034565a619?pvs=21),,,"September 12, 2024 4:54 AM","September 14, 2024 10:00 AM"
2,"The ""Puppy Honeymoon Phase"": 3 Bad Habits To Ditch In Your Dog's First Week Home (To Build Lasting Positive Behaviors)",,"Blog Post, Newsletter",Published,Puppies,,"August 16, 2024","August 17, 2024",https://www.fineanddandyaussiedoodles.com/post/the-puppy-honeymoon-phase-3-bad-habits-to-ditch-in-your-dog-s-first-week-home-to-build-lasting-p,Laney Content Call 02 – Interview Questions (https://www.notion.so/Laney-Content-Call-02-Interview-Questions-8dc537a47bcf41778632f75cb31f1502?pvs=21) ,,"[Instagram Post] The ""Puppy Honeymoon Phase"": 3 Bad Habits To Ditch In Your Dog's First Week Home (To Build Lasting Positive Behaviors) (https://www.notion.so/Instagram-Post-The-Puppy-Honeymoon-Phase-3-Bad-Habits-To-Ditch-In-Your-Dog-s-First-Week-Home-To-724f5ef80506438eac0cebb45c420460?pvs=21)",,"August 28, 2024 11:19 AM","September 14, 2024 10:06 AM"
2.1,"[Instagram Post] The ""Puppy Honeymoon Phase"": 3 Bad Habits To Ditch In Your Dog's First Week Home (To Build Lasting Positive Behaviors)",,Instagram Post,Upcoming,Puppies,,,,,,"The ""Puppy Honeymoon Phase"": 3 Bad Habits To Ditch In Your Dog's First Week Home (To Build Lasting Positive Behaviors) (https://www.notion.so/The-Puppy-Honeymoon-Phase-3-Bad-Habits-To-Ditch-In-Your-Dog-s-First-Week-Home-To-Build-Lasting-P-7ff9743d99f74790ab6b8c76dde66f10?pvs=21)",,,"September 12, 2024 4:55 AM","September 14, 2024 9:56 AM"
3,5 Questions You Should Consider When Deciding To Get An Aussie Doodle,,"Blog Post, Newsletter",Published,Preparation,,"August 28, 2024","August 29, 2024",https://www.fineanddandyaussiedoodles.com/post/5-questions-you-should-consider-when-deciding-to-get-an-aussie-doodle,Laney Content Call 03 – Interview Questions (https://www.notion.so/Laney-Content-Call-03-Interview-Questions-16eed123875d4defb52510ae2b4ad5e6?pvs=21) ,,[Instagram Post] 5 Questions You Should Consider When Deciding To Get An Aussie Doodle (https://www.notion.so/Instagram-Post-5-Questions-You-Should-Consider-When-Deciding-To-Get-An-Aussie-Doodle-9b72b91806214072b3a6222765256304?pvs=21),,"August 28, 2024 11:19 AM","September 14, 2024 10:09 AM"
3.1,[Instagram Post] 5 Questions You Should Consider When Deciding To Get An Aussie Doodle,,Instagram Post,Upcoming,,,,,,,5 Questions You Should Consider When Deciding To Get An Aussie Doodle (https://www.notion.so/5-Questions-You-Should-Consider-When-Deciding-To-Get-An-Aussie-Doodle-c2bee912413542fea44da3dee836a2eb?pvs=21),,,"September 12, 2024 4:55 AM","September 14, 2024 9:51 AM"
4,How To Successfully Bring Your Aussie Doodle Home This Holiday Season (Without Last-Minute Travel Chaos),5 Proven Tips For The Easiest Puppy Arrival Ever,"Blog Post, Newsletter",Published,Puppies,"Christmas Season, Holiday Travel","September 12, 2024","September 13, 2024",https://www.fineanddandyaussiedoodles.com/post/how-to-successfully-bring-your-aussie-doodle-home-this-holiday-season-without-last-minute-travel-ch,Laney Content Call 04 – Interview Questions (https://www.notion.so/Laney-Content-Call-04-Interview-Questions-f8f20478605a4118a39abd4099cebfbf?pvs=21) ,,[Instagram Post] How To Successfully Bring Your Aussie Doodle Home This Holiday Season (Without Last-Minute Travel Chaos) (https://www.notion.so/Instagram-Post-How-To-Successfully-Bring-Your-Aussie-Doodle-Home-This-Holiday-Season-Without-Last--d2ed36dde3f9497e94fb39c1eada6aed?pvs=21),,"September 13, 2024 2:07 PM","September 14, 2024 10:57 AM"
4.1,[Instagram Post] How To Successfully Bring Your Aussie Doodle Home This Holiday Season (Without Last-Minute Travel Chaos),5 Proven Tips For The Easiest Puppy Arrival Ever,Instagram Post,Upcoming,Puppies,"Christmas Season, Holiday Travel",,,,,How To Successfully Bring Your Aussie Doodle Home This Holiday Season (Without Last-Minute Travel Chaos) (https://www.notion.so/How-To-Successfully-Bring-Your-Aussie-Doodle-Home-This-Holiday-Season-Without-Last-Minute-Travel-Ch-1004d30935588065b440fb5afbebfe84?pvs=21),,"Dreaming of an Aussie Doodle under your Christmas tree, but stressing about holiday travel chaos? I've been there, and I've got you covered. 🎄🐾

Bringing home your new best friend during the holidays can actually be smooth and stress-free. Here's my tried-and-true gameplan:

1. Choose your perfect match (trust me, personality and compatibility matter!)
2. Book travel early (aim for October / November)
3. Prep essentials for the journey AND your arrival home
4. Nail down pickup details (always have a Plan B)
5. Create a cozy, safe welcome home

By following these steps, you're not just dodging stress — you're setting the stage for years of happiness with your new best friend. Imagine the difference between a chaotic arrival and a joyful, seamless transition. Your future self (and pup!) will thank you.

Ready to make your Aussie Doodle dreams a reality? I've got a full guide waiting for you.

Plus, for a limited time, get $500 off our Christmas puppies! This offer expires October 31st, so act soon before all the puppies are spoken for.

Click the link in my story or bio to get the full guide and browse our available puppies. Let's find your perfect match! 🐶♥️

#AussieDoodle #HolidayPuppy #NewDogTips #PetTravel #DoodleLife #PuppyPrep #AussieDoodleOwners #ChristmasDog #DogAdoption #NewPetOwner #DoodleCommunity #PetParentAdvice","September 13, 2024 2:07 PM","September 14, 2024 11:19 PM"
```

### Recap

And there ya have it: a rock-solid breakdown of the content database, its properties, and how to modify each piece. By now, you should have a clear understanding of what each variable represents and how to use it within this system.

With this setup in place, we'll be able to easily manage Laney's long-form and short-form content — because everything is categorized, trackable, and repurposable across multiple platforms, all accessible in one place.

### Instructions (Steps & Guidelines)

We'll be working with the `blog_posts` folder and the `laney's_content_database.csv` file. You'll create, read, update, and delete content in the CSV file (aka the "content database"), using the markdown files in the `blog_posts` folder as your inputs.

Here's the general process we'll roll with:

1. You'll add a new database entry to the `laney's_content_database.csv` file for every blog post in the `blog_posts` folder.
2. You'll add a new social post database entry for each blog post entry (immediately below it), following the instructions I've outlined here.
3. To make sure everything's working correctly, we'll tackle this in small batches to start. Let's go with 5 files at a time — I'll specify which ones to use (by giving you a range of file names that are numbered).

You'll ask for my feedback each time, and we'll make adjustments as we go.
