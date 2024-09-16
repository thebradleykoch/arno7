# Laney's Content Database Gameplan

## Goal (Task & Purpose)

The goal of this project is to create a comprehensive content database for my client, Laney. We're aiming to organize all of her long-form blog posts and their related short-form social posts in one place.

The database treats long-form posts (like newsletters and blog posts) as "hub" content, while treating short-form content (like Instagram posts) as the "spokes" that extend from the hub.

At the end of the day, this setup is designed to help us easily track, repurpose, and create content across different platforms (while keeping everything organized in one unified structure).

## Components (Pieces & Functions)

### Database Properties

The database uses specific properties — which I essentially think of like variables. These properties define the content and the relationships between hub content (blog posts) and spoke content (social posts). I've outlined the relevant properties for you below, including instructions on how to handle each one.

#### 1. Post Title

**Definition:**  
The title or headline of the post (regardless of whether it's long-form or short-form content).

**Instructions:**  

- For main posts (long-form content), use the exact title or headline from the blog post's file name, excluding the "FCD_{number}" suffix and the file extension.
- For social posts (spokes), prepend the corresponding hub post's title with a label like `[Instagram Post]` to distinguish it from the original long-form post's title.

#### 2. Subtitle / Description

**Definition:**  
The subtitle or brief description of the content.

**Instructions:**  

- If a subtitle is provided within the blog post content, use it here.
- If no subtitle exists, but there's a relevant excerpt or short description that fits, feel free to use that.
- Don't force-fit this — only fill this property out if it makes sense to.

#### 3. Content Type

**Definition:**  
This defines the type of content. It's a select property with the following options:  
`Newsletter`, `Blog Post`, `Podcast`, `Video`, `Instagram Post`, `Facebook Post`, `Tweet`, `Twitter Thread`, `LinkedIn Post`, `Email`, `Email Sequence`, `Landing Page`, `Sales Page`, `Course Module`.

**Instructions:**  

- Choose the appropriate content type from the list.
- Focus mainly on the first few options (newsletter, blog post, Instagram post, etc.), since we're dealing primarily with long-form and short-form content, not sales pages or emails yet.

#### 4. Status

**Definition:**  
A select property with four options: `Upcoming`, `Unknown`, `In progress`, and `Published`.

**Instructions:**  

- `Upcoming`: Use for posts that are planned but not created yet.
- `Unknown`: Use for social posts (spokes) that have a corresponding main post (hub) which has already been published, and this social post's "status" property is still blank. (I haven't verified whether any previously existing social posts that are directly related have been published yet, that's why.)
- `In progress`: For content that Laney and I are actively working on.
- `Published`: For content that's completed and live.

#### 5. Main Topic

**Definition:**  
The primary topic of the post. This is a select property that will usually have 1 main topic, but can include up to 2-3 (if needed for more context and specificity).

**Instructions:**  

- Do your best to choose just one "main topic" whenever possible. But if you genuinely need to add more context or specificity (by combining or pairing multiple topics together) you can choose up to 2 or 3.

#### 6. Subtopics

**Definition:**  
Relevant supporting topics that provide more context or depth to the main topic (but only if these subtopics are already present within the original post).

**Instructions:**  

- Choose between 3-5 subtopics.
- Keep this list tight and on-point, unless more comprehensive context is needed.

#### 7. Action Date

**Definition:**  
The date I ghostwrote (or will ghostwrite) the post.

**Instructions:**  

- Leave this field blank unless I've already specified the action date.

#### 8. Post Date

**Definition:**  
The date when the post was (or will be) published.

**Instructions:**  

- Leave blank unless a post date is already provided.

#### 9. Published Link

**Definition:**  
The URL of the published blog post.

**Instructions:**  

- Extract this URL from the markdown-formatted link found at the end of the blog post content (usually labeled with CTA text like "Read On Blog").
- Paste the link into this property.

#### 10. Main Post (Hub)

**Definition:**  
A relation property linking a social post (spoke) to its corresponding main post (hub).

**Instructions:**  

- If you're working with a main post (hub) item, leave this blank (because it is the main post).
- If you're working with a social post (spoke) item, copy and paste the title of the corresponding blog post here using a markdown-formatted link, like `[Blog Post Title](placeholder_url)`.

#### 11. Social Posts (Spokes)

**Definition:**  
A relation property linking a main post (hub) to its corresponding social posts (spokes).

**Instructions:**  

- If you're working with a social post (spoke) item, leave this blank (because it is the spoke).
- If you're working with a main post (hub) item, copy and paste its own title into this property using a markdown-formatted link, like `[Blog Post Title](placeholder_url)`.

#### 12. Related Resources

**Definition:**  
A field for any links or resources related to the post.

**Instructions:**  

- Leave this blank unless I've already included the resources.

#### 13. Instagram Caption

**Definition:**  
The caption for the Instagram post.

**Instructions:**  

- Leave this blank for now. I'll throw you more instructions on this part later.

#### 14. First Created

**Definition:**  
The date and time when the database item was first created.

**Instructions:**  

- Leave this field blank (unless it's already filled in).

#### 15. Last Edited

**Definition:**  
The date and time when the database item was last edited.

**Instructions:**  

- Leave this blank (unless it's already populated).

And there ya have it: a rock-solid breakdown of the content database,  its properties, and how to modify each piece. By now, you should have a clear understanding of what each variable represents and how to use it within this system.

With this setup in place, we'll be able to easily manage Laney's long-form and short-form content — because everything is categorized, trackable, and repurposable across multiple platforms, all accessible in one place.

### Instructions (Steps & Guidelines)

We'll be working with the `blog_posts` folder and the `laney's_content_database.csv` file. You'll create, read, update, and delete content in the CSV file (aka the "content database"), using the markdown files in the `blog_posts` folder as your inputs.

Here's the general process we'll roll with:

1. You'll add a new database entry to the `laney's_content_database.csv` file for every blog post in the `blog_posts` folder.
2. You'll add a new social post database entry for each blog post entry (immediately below it), following the instructions I've outlined here.
3. To make sure everything's working correctly, we'll tackle this in small batches to start. Let's go with 5 files at a time — I'll specify which ones to use (by giving you a range of file names that are numbered).

You'll ask for my feedback each time, and we'll make adjustments as we go.
