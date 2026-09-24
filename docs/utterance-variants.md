# Ways to say each candidate intent

Version 2 now defines structured schemas for all 223 intents. See
[the current model and workflow](structured-intents.md). Historical counts and
example lists below describe the original audit; use `data/catalog.json` and
the browser explorer for current definitions.

There are **ten labeled phrases for each of 223 intents** (2,230 total).
The first two are illustrative phrases from [intents.json](../data/intents.json)
or [candidate-utterances.tsv](../data/candidate-utterances.tsv). The other
eight are synthetic request frames applied to those two phrases, with
[imperative clause overrides](../data/utterance-clauses.tsv) where needed.
The [machine-readable JSON](../data/utterances.json) records each phrase's
intent, variant number, origin, base variant, frame, and arguments when known.
These examples have **not** been tested in any voice application.
The request frames add surface variation, but they are correlated and
must not be treated as ten independent ways people naturally speak.
Phrases under one intent can use different example argument values.

The candidate IDs still need [schema review](intent-coverage.md),
especially where a tool action or control may overlap another intent.
Do not score slot extraction on rows whose `arguments` value is `null`.
[Verification](verification.md) records which source tests actually ran.

## agent

### `agent.request` (review needed)

1. Ask the assistant to summarize this page
2. Have the agent explain what is on screen
3. Please ask the assistant to summarize this page.
4. Could you ask the assistant to summarize this page?
5. Ask the assistant to summarize this page, please.
6. I need you to ask the assistant to summarize this page.
7. Please have the agent explain what is on screen.
8. Could you have the agent explain what is on screen?
9. Have the agent explain what is on screen, please.
10. I need you to have the agent explain what is on screen.

## app

### `app.close` (typed)

1. Close Discord
2. Close the browser window
3. Please close Discord.
4. Could you close Discord?
5. Close Discord, please.
6. I need you to close Discord.
7. Please close the browser window.
8. Could you close the browser window?
9. Close the browser window, please.
10. I need you to close the browser window.

### `app.focus` (typed)

1. Focus Firefox
2. Bring my browser forward
3. Please focus Firefox.
4. Could you focus Firefox?
5. Focus Firefox, please.
6. I need you to focus Firefox.
7. Please bring my browser forward.
8. Could you bring my browser forward?
9. Bring my browser forward, please.
10. I need you to bring my browser forward.

### `app.launch` (typed)

1. Open Firefox
2. Start the browser
3. Please open Firefox.
4. Could you open Firefox?
5. Open Firefox, please.
6. I need you to open Firefox.
7. Please start the browser.
8. Could you start the browser?
9. Start the browser, please.
10. I need you to start the browser.

### `app.list` (review needed)

1. Show my open apps
2. Which applications are running?
3. Please show my open apps.
4. Could you show my open apps?
5. Show my open apps, please.
6. I need you to show my open apps.
7. Please list the running applications.
8. Could you list the running applications?
9. List the running applications, please.
10. I need you to list the running applications.

## audio

### `audio.mute` (typed)

1. Mute the sound
2. Mute audio
3. Please mute the sound.
4. Could you mute the sound?
5. Mute the sound, please.
6. I need you to mute the sound.
7. Please mute audio.
8. Could you mute audio?
9. Mute audio, please.
10. I need you to mute audio.

### `audio.mute_toggle` (review needed)

1. Toggle the sound mute
2. Switch mute on or off
3. Please toggle the sound mute.
4. Could you toggle the sound mute?
5. Toggle the sound mute, please.
6. I need you to toggle the sound mute.
7. Please switch mute on or off.
8. Could you switch mute on or off?
9. Switch mute on or off, please.
10. I need you to switch mute on or off.

### `audio.unmute` (typed)

1. Unmute the sound
2. Turn sound back on
3. Please unmute the sound.
4. Could you unmute the sound?
5. Unmute the sound, please.
6. I need you to unmute the sound.
7. Please turn sound back on.
8. Could you turn sound back on?
9. Turn sound back on, please.
10. I need you to turn sound back on.

### `audio.volume_down` (typed)

1. Turn the volume down
2. Make it quieter
3. Please turn the volume down.
4. Could you turn the volume down?
5. Turn the volume down, please.
6. I need you to turn the volume down.
7. Please make it quieter.
8. Could you make it quieter?
9. Make it quieter, please.
10. I need you to make it quieter.

### `audio.volume_set` (review needed)

1. Set the volume to 40 percent
2. Make the sound level 40 percent
3. Please set the volume to 40 percent.
4. Could you set the volume to 40 percent?
5. Set the volume to 40 percent, please.
6. I need you to set the volume to 40 percent.
7. Please make the sound level 40 percent.
8. Could you make the sound level 40 percent?
9. Make the sound level 40 percent, please.
10. I need you to make the sound level 40 percent.

### `audio.volume_up` (typed)

1. Turn the volume up
2. Make it louder
3. Please turn the volume up.
4. Could you turn the volume up?
5. Turn the volume up, please.
6. I need you to turn the volume up.
7. Please make it louder.
8. Could you make it louder?
9. Make it louder, please.
10. I need you to make it louder.

## browser

### `browser.close` (review needed)

1. Close the browser
2. Shut the browser
3. Please close the browser.
4. Could you close the browser?
5. Close the browser, please.
6. I need you to close the browser.
7. Please shut the browser.
8. Could you shut the browser?
9. Shut the browser, please.
10. I need you to shut the browser.

### `browser.download` (review needed)

1. Download this file
2. Save that download from the page
3. Please download this file.
4. Could you download this file?
5. Download this file, please.
6. I need you to download this file.
7. Please save that download from the page.
8. Could you save that download from the page?
9. Save that download from the page, please.
10. I need you to save that download from the page.

### `browser.drag` (review needed)

1. Drag that item to the folder
2. Move this page element over there
3. Please drag that item to the folder.
4. Could you drag that item to the folder?
5. Drag that item to the folder, please.
6. I need you to drag that item to the folder.
7. Please move this page element over there.
8. Could you move this page element over there?
9. Move this page element over there, please.
10. I need you to move this page element over there.

### `browser.element_click` (typed)

1. Click the sign in button
2. Click the highlighted link
3. Please click the sign in button.
4. Could you click the sign in button?
5. Click the sign in button, please.
6. I need you to click the sign in button.
7. Please click the highlighted link.
8. Could you click the highlighted link?
9. Click the highlighted link, please.
10. I need you to click the highlighted link.

### `browser.element_focus` (review needed)

1. Focus the search box
2. Put the cursor in the search field
3. Please focus the search box.
4. Could you focus the search box?
5. Focus the search box, please.
6. I need you to focus the search box.
7. Please put the cursor in the search field.
8. Could you put the cursor in the search field?
9. Put the cursor in the search field, please.
10. I need you to put the cursor in the search field.

### `browser.element_hover` (review needed)

1. Hover over that menu
2. Move the pointer over this link
3. Please hover over that menu.
4. Could you hover over that menu?
5. Hover over that menu, please.
6. I need you to hover over that menu.
7. Please move the pointer over this link.
8. Could you move the pointer over this link?
9. Move the pointer over this link, please.
10. I need you to move the pointer over this link.

### `browser.form_check` (review needed)

1. Check the remember me box
2. Tick the terms checkbox
3. Please check the remember me box.
4. Could you check the remember me box?
5. Check the remember me box, please.
6. I need you to check the remember me box.
7. Please tick the terms checkbox.
8. Could you tick the terms checkbox?
9. Tick the terms checkbox, please.
10. I need you to tick the terms checkbox.

### `browser.form_fill` (typed)

1. Fill email with me@example.com
2. Type my name into the form
3. Please fill email with me@example.com.
4. Could you fill email with me@example.com?
5. Fill email with me@example.com, please.
6. I need you to fill email with me@example.com.
7. Please type my name into the form.
8. Could you type my name into the form?
9. Type my name into the form, please.
10. I need you to type my name into the form.

### `browser.form_select` (review needed)

1. Select Canada from the country menu
2. Choose the second option in that dropdown
3. Please select Canada from the country menu.
4. Could you select Canada from the country menu?
5. Select Canada from the country menu, please.
6. I need you to select Canada from the country menu.
7. Please choose the second option in that dropdown.
8. Could you choose the second option in that dropdown?
9. Choose the second option in that dropdown, please.
10. I need you to choose the second option in that dropdown.

### `browser.handoff` (review needed)

1. Hand this page to the browser agent
2. Let the browser agent take over this page
3. Please hand this page to the browser agent.
4. Could you hand this page to the browser agent?
5. Hand this page to the browser agent, please.
6. I need you to hand this page to the browser agent.
7. Please let the browser agent take over this page.
8. Could you let the browser agent take over this page?
9. Let the browser agent take over this page, please.
10. I need you to let the browser agent take over this page.

### `browser.navigate` (typed)

1. Open GitHub
2. Go to example.com
3. Please open GitHub.
4. Could you open GitHub?
5. Open GitHub, please.
6. I need you to open GitHub.
7. Please go to example.com.
8. Could you go to example.com?
9. Go to example.com, please.
10. I need you to go to example.com.

### `browser.open` (review needed)

1. Open the browser
2. Bring up the browser
3. Please open the browser.
4. Could you open the browser?
5. Open the browser, please.
6. I need you to open the browser.
7. Please bring up the browser.
8. Could you bring up the browser?
9. Bring up the browser, please.
10. I need you to bring up the browser.

### `browser.page_back` (typed)

1. Go back in the browser
2. Previous page
3. Please go back in the browser.
4. Could you go back in the browser?
5. Go back in the browser, please.
6. I need you to go back in the browser.
7. Please go to the previous page.
8. Could you go to the previous page?
9. Go to the previous page, please.
10. I need you to go to the previous page.

### `browser.page_forward` (review needed)

1. Go forward one page
2. Return to the next page in browser history
3. Please go forward one page.
4. Could you go forward one page?
5. Go forward one page, please.
6. I need you to go forward one page.
7. Please return to the next page in browser history.
8. Could you return to the next page in browser history?
9. Return to the next page in browser history, please.
10. I need you to return to the next page in browser history.

### `browser.page_read` (typed)

1. Read this page
2. Summarize the current page
3. Please read this page.
4. Could you read this page?
5. Read this page, please.
6. I need you to read this page.
7. Please summarize the current page.
8. Could you summarize the current page?
9. Summarize the current page, please.
10. I need you to summarize the current page.

### `browser.page_reload` (review needed)

1. Reload this page
2. Refresh the current website
3. Please reload this page.
4. Could you reload this page?
5. Reload this page, please.
6. I need you to reload this page.
7. Please refresh the current website.
8. Could you refresh the current website?
9. Refresh the current website, please.
10. I need you to refresh the current website.

### `browser.page_scroll` (typed)

1. Scroll down
2. Scroll the page to the left
3. Please scroll down.
4. Could you scroll down?
5. Scroll down, please.
6. I need you to scroll down.
7. Please scroll the page to the left.
8. Could you scroll the page to the left?
9. Scroll the page to the left, please.
10. I need you to scroll the page to the left.

### `browser.tab_close` (typed)

1. Close this tab
2. Close all browser tabs
3. Please close this tab.
4. Could you close this tab?
5. Close this tab, please.
6. I need you to close this tab.
7. Please close all browser tabs.
8. Could you close all browser tabs?
9. Close all browser tabs, please.
10. I need you to close all browser tabs.

### `browser.tab_list` (review needed)

1. List my browser tabs
2. Which tabs are open?
3. Please list my browser tabs.
4. Could you list my browser tabs?
5. List my browser tabs, please.
6. I need you to list my browser tabs.
7. Please show the open browser tabs.
8. Could you show the open browser tabs?
9. Show the open browser tabs, please.
10. I need you to show the open browser tabs.

### `browser.tab_new` (typed)

1. Open a new GitHub tab
2. Create a new tab
3. Please open a new GitHub tab.
4. Could you open a new GitHub tab?
5. Open a new GitHub tab, please.
6. I need you to open a new GitHub tab.
7. Please create a new tab.
8. Could you create a new tab?
9. Create a new tab, please.
10. I need you to create a new tab.

### `browser.tab_switch` (typed)

1. Switch to tab two
2. Go to the GitHub tab
3. Please switch to tab two.
4. Could you switch to tab two?
5. Switch to tab two, please.
6. I need you to switch to tab two.
7. Please go to the GitHub tab.
8. Could you go to the GitHub tab?
9. Go to the GitHub tab, please.
10. I need you to go to the GitHub tab.

### `browser.tabs_clear` (review needed)

1. Clear every open browser tab
2. Remove all tabs from the browser
3. Please clear every open browser tab.
4. Could you clear every open browser tab?
5. Clear every open browser tab, please.
6. I need you to clear every open browser tab.
7. Please remove all tabs from the browser.
8. Could you remove all tabs from the browser?
9. Remove all tabs from the browser, please.
10. I need you to remove all tabs from the browser.

### `browser.upload` (review needed)

1. Upload the report to this page
2. Choose the report file for this form
3. Please upload the report to this page.
4. Could you upload the report to this page?
5. Upload the report to this page, please.
6. I need you to upload the report to this page.
7. Please choose the report file for this form.
8. Could you choose the report file for this form?
9. Choose the report file for this form, please.
10. I need you to choose the report file for this form.

### `browser.wait` (review needed)

1. Wait for the page to load
2. Pause until the page is ready
3. Please wait for the page to load.
4. Could you wait for the page to load?
5. Wait for the page to load, please.
6. I need you to wait for the page to load.
7. Please pause until the page is ready.
8. Could you pause until the page is ready?
9. Pause until the page is ready, please.
10. I need you to pause until the page is ready.

## calendar

### `calendar.events` (review needed)

1. What events are on my calendar today?
2. Show today's calendar events
3. Please tell me what is on my calendar today.
4. Could you tell me what is on my calendar today?
5. Tell me what is on my calendar today, please.
6. I need you to tell me what is on my calendar today.
7. Please show today's calendar events.
8. Could you show today's calendar events?
9. Show today's calendar events, please.
10. I need you to show today's calendar events.

### `calendar.list` (review needed)

1. List my calendars
2. Which calendars can I use?
3. Please list my calendars.
4. Could you list my calendars?
5. List my calendars, please.
6. I need you to list my calendars.
7. Please show the available calendars.
8. Could you show the available calendars?
9. Show the available calendars, please.
10. I need you to show the available calendars.

### `calendar.todo_create` (review needed)

1. Add a calendar to-do to call Sam
2. Create a to-do in my calendar for calling Sam
3. Please add a calendar to-do to call Sam.
4. Could you add a calendar to-do to call Sam?
5. Add a calendar to-do to call Sam, please.
6. I need you to add a calendar to-do to call Sam.
7. Please create a to-do in my calendar for calling Sam.
8. Could you create a to-do in my calendar for calling Sam?
9. Create a to-do in my calendar for calling Sam, please.
10. I need you to create a to-do in my calendar for calling Sam.

### `calendar.todo_list` (review needed)

1. Show my calendar to-dos
2. What to-dos are in my calendar?
3. Please show my calendar to-dos.
4. Could you show my calendar to-dos?
5. Show my calendar to-dos, please.
6. I need you to show my calendar to-dos.
7. Please list my calendar to-dos.
8. Could you list my calendar to-dos?
9. List my calendar to-dos, please.
10. I need you to list my calendar to-dos.

## camera

### `camera.inspect` (review needed)

1. Look at the camera image
2. Describe what the camera sees
3. Please look at the camera image.
4. Could you look at the camera image?
5. Look at the camera image, please.
6. I need you to look at the camera image.
7. Please describe what the camera sees.
8. Could you describe what the camera sees?
9. Describe what the camera sees, please.
10. I need you to describe what the camera sees.

## clipboard

### `clipboard.manage` (review needed)

1. Open clipboard history
2. Show the clipboard manager
3. Please open clipboard history.
4. Could you open clipboard history?
5. Open clipboard history, please.
6. I need you to open clipboard history.
7. Please show the clipboard manager.
8. Could you show the clipboard manager?
9. Show the clipboard manager, please.
10. I need you to show the clipboard manager.

### `clipboard.read` (typed)

1. What is on my clipboard?
2. Read the clipboard
3. Please tell me what is on my clipboard.
4. Could you tell me what is on my clipboard?
5. Tell me what is on my clipboard, please.
6. I need you to tell me what is on my clipboard.
7. Please read the clipboard.
8. Could you read the clipboard?
9. Read the clipboard, please.
10. I need you to read the clipboard.

### `clipboard.write` (typed)

1. Copy hello to the clipboard
2. Put this text on my clipboard
3. Please copy hello to the clipboard.
4. Could you copy hello to the clipboard?
5. Copy hello to the clipboard, please.
6. I need you to copy hello to the clipboard.
7. Please put this text on my clipboard.
8. Could you put this text on my clipboard?
9. Put this text on my clipboard, please.
10. I need you to put this text on my clipboard.

## coding

### `coding.agent.explain` (review needed)

1. Explain what coding agent one is doing
2. Summarize agent one's work
3. Please explain what coding agent one is doing.
4. Could you explain what coding agent one is doing?
5. Explain what coding agent one is doing, please.
6. I need you to explain what coding agent one is doing.
7. Please summarize agent one's work.
8. Could you summarize agent one's work?
9. Summarize agent one's work, please.
10. I need you to summarize agent one's work.

### `coding.agent.focus` (review needed)

1. Focus coding agent one
2. Switch to agent one's pane
3. Please focus coding agent one.
4. Could you focus coding agent one?
5. Focus coding agent one, please.
6. I need you to focus coding agent one.
7. Please switch to agent one's pane.
8. Could you switch to agent one's pane?
9. Switch to agent one's pane, please.
10. I need you to switch to agent one's pane.

### `coding.agent.get` (review needed)

1. Show coding agent one's details
2. Get information about agent one
3. Please show coding agent one's details.
4. Could you show coding agent one's details?
5. Show coding agent one's details, please.
6. I need you to show coding agent one's details.
7. Please get information about agent one.
8. Could you get information about agent one?
9. Get information about agent one, please.
10. I need you to get information about agent one.

### `coding.agent.list` (review needed)

1. List the coding agents
2. Which coding agents are running?
3. Please list the coding agents.
4. Could you list the coding agents?
5. List the coding agents, please.
6. I need you to list the coding agents.
7. Please show the running coding agents.
8. Could you show the running coding agents?
9. Show the running coding agents, please.
10. I need you to show the running coding agents.

### `coding.agent.prompt` (review needed)

1. Prompt agent one to review this change
2. Ask coding agent one to review this change
3. Please prompt agent one to review this change.
4. Could you prompt agent one to review this change?
5. Prompt agent one to review this change, please.
6. I need you to prompt agent one to review this change.
7. Please ask coding agent one to review this change.
8. Could you ask coding agent one to review this change?
9. Ask coding agent one to review this change, please.
10. I need you to ask coding agent one to review this change.

### `coding.agent.read` (review needed)

1. Read coding agent one's output
2. Show what agent one said
3. Please read coding agent one's output.
4. Could you read coding agent one's output?
5. Read coding agent one's output, please.
6. I need you to read coding agent one's output.
7. Please show what agent one said.
8. Could you show what agent one said?
9. Show what agent one said, please.
10. I need you to show what agent one said.

### `coding.agent.rename` (review needed)

1. Rename coding agent one to reviewer
2. Call agent one reviewer
3. Please rename coding agent one to reviewer.
4. Could you rename coding agent one to reviewer?
5. Rename coding agent one to reviewer, please.
6. I need you to rename coding agent one to reviewer.
7. Please call agent one reviewer.
8. Could you call agent one reviewer?
9. Call agent one reviewer, please.
10. I need you to call agent one reviewer.

### `coding.agent.send_keys` (review needed)

1. Send Enter to coding agent one
2. Press Escape in agent one's pane
3. Please send Enter to coding agent one.
4. Could you send Enter to coding agent one?
5. Send Enter to coding agent one, please.
6. I need you to send Enter to coding agent one.
7. Please press Escape in agent one's pane.
8. Could you press Escape in agent one's pane?
9. Press Escape in agent one's pane, please.
10. I need you to press Escape in agent one's pane.

### `coding.agent.start` (review needed)

1. Start a coding agent for this task
2. Launch a new coding agent
3. Please start a coding agent for this task.
4. Could you start a coding agent for this task?
5. Start a coding agent for this task, please.
6. I need you to start a coding agent for this task.
7. Please launch a new coding agent.
8. Could you launch a new coding agent?
9. Launch a new coding agent, please.
10. I need you to launch a new coding agent.

### `coding.api.snapshot` (review needed)

1. Capture the coding API snapshot
2. Show the current coding API snapshot
3. Please capture the coding API snapshot.
4. Could you capture the coding API snapshot?
5. Capture the coding API snapshot, please.
6. I need you to capture the coding API snapshot.
7. Please show the current coding API snapshot.
8. Could you show the current coding API snapshot?
9. Show the current coding API snapshot, please.
10. I need you to show the current coding API snapshot.

### `coding.notification.show` (review needed)

1. Show coding notifications
2. Open the coding notification list
3. Please show coding notifications.
4. Could you show coding notifications?
5. Show coding notifications, please.
6. I need you to show coding notifications.
7. Please open the coding notification list.
8. Could you open the coding notification list?
9. Open the coding notification list, please.
10. I need you to open the coding notification list.

### `coding.pane.close` (review needed)

1. Close this coding pane
2. Remove the current pane
3. Please close this coding pane.
4. Could you close this coding pane?
5. Close this coding pane, please.
6. I need you to close this coding pane.
7. Please remove the current pane.
8. Could you remove the current pane?
9. Remove the current pane, please.
10. I need you to remove the current pane.

### `coding.pane.current` (review needed)

1. Which coding pane is active?
2. Show the current pane
3. Please show the active coding pane.
4. Could you show the active coding pane?
5. Show the active coding pane, please.
6. I need you to show the active coding pane.
7. Please show the current pane.
8. Could you show the current pane?
9. Show the current pane, please.
10. I need you to show the current pane.

### `coding.pane.edges` (review needed)

1. Show this pane's edges
2. Get the boundaries of the current pane
3. Please show this pane's edges.
4. Could you show this pane's edges?
5. Show this pane's edges, please.
6. I need you to show this pane's edges.
7. Please get the boundaries of the current pane.
8. Could you get the boundaries of the current pane?
9. Get the boundaries of the current pane, please.
10. I need you to get the boundaries of the current pane.

### `coding.pane.focus` (review needed)

1. Focus the pane on the right
2. Switch to the right coding pane
3. Please focus the pane on the right.
4. Could you focus the pane on the right?
5. Focus the pane on the right, please.
6. I need you to focus the pane on the right.
7. Please switch to the right coding pane.
8. Could you switch to the right coding pane?
9. Switch to the right coding pane, please.
10. I need you to switch to the right coding pane.

### `coding.pane.get` (review needed)

1. Show details for pane one
2. Get pane one's information
3. Please show details for pane one.
4. Could you show details for pane one?
5. Show details for pane one, please.
6. I need you to show details for pane one.
7. Please get pane one's information.
8. Could you get pane one's information?
9. Get pane one's information, please.
10. I need you to get pane one's information.

### `coding.pane.input` (review needed)

1. Type the command into pane one
2. Enter this text in the coding pane
3. Please type the command into pane one.
4. Could you type the command into pane one?
5. Type the command into pane one, please.
6. I need you to type the command into pane one.
7. Please enter this text in the coding pane.
8. Could you enter this text in the coding pane?
9. Enter this text in the coding pane, please.
10. I need you to enter this text in the coding pane.

### `coding.pane.layout` (review needed)

1. Show the pane layout
2. How are my coding panes arranged?
3. Please show the pane layout.
4. Could you show the pane layout?
5. Show the pane layout, please.
6. I need you to show the pane layout.
7. Please tell me how the coding panes are arranged.
8. Could you tell me how the coding panes are arranged?
9. Tell me how the coding panes are arranged, please.
10. I need you to tell me how the coding panes are arranged.

### `coding.pane.list` (review needed)

1. List the coding panes
2. Which panes are open?
3. Please list the coding panes.
4. Could you list the coding panes?
5. List the coding panes, please.
6. I need you to list the coding panes.
7. Please show the open coding panes.
8. Could you show the open coding panes?
9. Show the open coding panes, please.
10. I need you to show the open coding panes.

### `coding.pane.move` (review needed)

1. Move this pane to the left
2. Put the current pane on the left
3. Please move this pane to the left.
4. Could you move this pane to the left?
5. Move this pane to the left, please.
6. I need you to move this pane to the left.
7. Please put the current pane on the left.
8. Could you put the current pane on the left?
9. Put the current pane on the left, please.
10. I need you to put the current pane on the left.

### `coding.pane.neighbor` (review needed)

1. Which pane is next to this one?
2. Find the neighboring pane
3. Please show the pane next to this one.
4. Could you show the pane next to this one?
5. Show the pane next to this one, please.
6. I need you to show the pane next to this one.
7. Please find the neighboring pane.
8. Could you find the neighboring pane?
9. Find the neighboring pane, please.
10. I need you to find the neighboring pane.

### `coding.pane.process_info` (review needed)

1. What process is running in this pane?
2. Show the pane's process information
3. Please tell me what process is running in this pane.
4. Could you tell me what process is running in this pane?
5. Tell me what process is running in this pane, please.
6. I need you to tell me what process is running in this pane.
7. Please show the pane's process information.
8. Could you show the pane's process information?
9. Show the pane's process information, please.
10. I need you to show the pane's process information.

### `coding.pane.read` (review needed)

1. Read the current coding pane
2. Show the text in this pane
3. Please read the current coding pane.
4. Could you read the current coding pane?
5. Read the current coding pane, please.
6. I need you to read the current coding pane.
7. Please show the text in this pane.
8. Could you show the text in this pane?
9. Show the text in this pane, please.
10. I need you to show the text in this pane.

### `coding.pane.rename` (review needed)

1. Rename this pane to tests
2. Call the current pane tests
3. Please rename this pane to tests.
4. Could you rename this pane to tests?
5. Rename this pane to tests, please.
6. I need you to rename this pane to tests.
7. Please call the current pane tests.
8. Could you call the current pane tests?
9. Call the current pane tests, please.
10. I need you to call the current pane tests.

### `coding.pane.resize` (review needed)

1. Make this pane wider
2. Increase the current pane's width
3. Please make this pane wider.
4. Could you make this pane wider?
5. Make this pane wider, please.
6. I need you to make this pane wider.
7. Please increase the current pane's width.
8. Could you increase the current pane's width?
9. Increase the current pane's width, please.
10. I need you to increase the current pane's width.

### `coding.pane.run` (review needed)

1. Run the tests in this pane
2. Execute the test command in the current pane
3. Please run the tests in this pane.
4. Could you run the tests in this pane?
5. Run the tests in this pane, please.
6. I need you to run the tests in this pane.
7. Please execute the test command in the current pane.
8. Could you execute the test command in the current pane?
9. Execute the test command in the current pane, please.
10. I need you to execute the test command in the current pane.

### `coding.pane.send_keys` (review needed)

1. Send Control C to this pane
2. Press Enter in the current pane
3. Please send Control C to this pane.
4. Could you send Control C to this pane?
5. Send Control C to this pane, please.
6. I need you to send Control C to this pane.
7. Please press Enter in the current pane.
8. Could you press Enter in the current pane?
9. Press Enter in the current pane, please.
10. I need you to press Enter in the current pane.

### `coding.pane.send_text` (review needed)

1. Send this text to the current pane
2. Paste the following text into this pane
3. Please send this text to the current pane.
4. Could you send this text to the current pane?
5. Send this text to the current pane, please.
6. I need you to send this text to the current pane.
7. Please paste the following text into this pane.
8. Could you paste the following text into this pane?
9. Paste the following text into this pane, please.
10. I need you to paste the following text into this pane.

### `coding.pane.split` (review needed)

1. Split this pane vertically
2. Create a pane beside this one
3. Please split this pane vertically.
4. Could you split this pane vertically?
5. Split this pane vertically, please.
6. I need you to split this pane vertically.
7. Please create a pane beside this one.
8. Could you create a pane beside this one?
9. Create a pane beside this one, please.
10. I need you to create a pane beside this one.

### `coding.pane.swap` (review needed)

1. Swap this pane with the one on the right
2. Exchange these two panes
3. Please swap this pane with the one on the right.
4. Could you swap this pane with the one on the right?
5. Swap this pane with the one on the right, please.
6. I need you to swap this pane with the one on the right.
7. Please exchange these two panes.
8. Could you exchange these two panes?
9. Exchange these two panes, please.
10. I need you to exchange these two panes.

### `coding.pane.zoom` (review needed)

1. Zoom this pane
2. Make the current pane fill the view
3. Please zoom this pane.
4. Could you zoom this pane?
5. Zoom this pane, please.
6. I need you to zoom this pane.
7. Please make the current pane fill the view.
8. Could you make the current pane fill the view?
9. Make the current pane fill the view, please.
10. I need you to make the current pane fill the view.

### `coding.server.reload_config` (review needed)

1. Reload the coding server configuration
2. Apply the server config again
3. Please reload the coding server configuration.
4. Could you reload the coding server configuration?
5. Reload the coding server configuration, please.
6. I need you to reload the coding server configuration.
7. Please apply the server config again.
8. Could you apply the server config again?
9. Apply the server config again, please.
10. I need you to apply the server config again.

### `coding.server.stop` (review needed)

1. Stop the coding server
2. Shut down the coding server
3. Please stop the coding server.
4. Could you stop the coding server?
5. Stop the coding server, please.
6. I need you to stop the coding server.
7. Please shut down the coding server.
8. Could you shut down the coding server?
9. Shut down the coding server, please.
10. I need you to shut down the coding server.

### `coding.session.delete` (review needed)

1. Delete coding session one
2. Remove the saved coding session
3. Please delete coding session one.
4. Could you delete coding session one?
5. Delete coding session one, please.
6. I need you to delete coding session one.
7. Please remove the saved coding session.
8. Could you remove the saved coding session?
9. Remove the saved coding session, please.
10. I need you to remove the saved coding session.

### `coding.session.list` (review needed)

1. List coding sessions
2. Which coding sessions exist?
3. Please list coding sessions.
4. Could you list coding sessions?
5. List coding sessions, please.
6. I need you to list coding sessions.
7. Please show the coding sessions.
8. Could you show the coding sessions?
9. Show the coding sessions, please.
10. I need you to show the coding sessions.

### `coding.session.stop` (review needed)

1. Stop coding session one
2. End the active coding session
3. Please stop coding session one.
4. Could you stop coding session one?
5. Stop coding session one, please.
6. I need you to stop coding session one.
7. Please end the active coding session.
8. Could you end the active coding session?
9. End the active coding session, please.
10. I need you to end the active coding session.

### `coding.status` (review needed)

1. Show coding status
2. What is the coding system doing?
3. Please show coding status.
4. Could you show coding status?
5. Show coding status, please.
6. I need you to show coding status.
7. Please tell me what the coding system is doing.
8. Could you tell me what the coding system is doing?
9. Tell me what the coding system is doing, please.
10. I need you to tell me what the coding system is doing.

### `coding.tab.close` (review needed)

1. Close this coding tab
2. Remove the current tab
3. Please close this coding tab.
4. Could you close this coding tab?
5. Close this coding tab, please.
6. I need you to close this coding tab.
7. Please remove the current tab.
8. Could you remove the current tab?
9. Remove the current tab, please.
10. I need you to remove the current tab.

### `coding.tab.create` (review needed)

1. Create a coding tab
2. Open a new coding tab
3. Please create a coding tab.
4. Could you create a coding tab?
5. Create a coding tab, please.
6. I need you to create a coding tab.
7. Please open a new coding tab.
8. Could you open a new coding tab?
9. Open a new coding tab, please.
10. I need you to open a new coding tab.

### `coding.tab.focus` (review needed)

1. Focus coding tab two
2. Switch to the second coding tab
3. Please focus coding tab two.
4. Could you focus coding tab two?
5. Focus coding tab two, please.
6. I need you to focus coding tab two.
7. Please switch to the second coding tab.
8. Could you switch to the second coding tab?
9. Switch to the second coding tab, please.
10. I need you to switch to the second coding tab.

### `coding.tab.get` (review needed)

1. Show details for coding tab two
2. Get information about tab two
3. Please show details for coding tab two.
4. Could you show details for coding tab two?
5. Show details for coding tab two, please.
6. I need you to show details for coding tab two.
7. Please get information about tab two.
8. Could you get information about tab two?
9. Get information about tab two, please.
10. I need you to get information about tab two.

### `coding.tab.list` (review needed)

1. List coding tabs
2. Which coding tabs are open?
3. Please list coding tabs.
4. Could you list coding tabs?
5. List coding tabs, please.
6. I need you to list coding tabs.
7. Please show the open coding tabs.
8. Could you show the open coding tabs?
9. Show the open coding tabs, please.
10. I need you to show the open coding tabs.

### `coding.tab.rename` (review needed)

1. Rename this coding tab to review
2. Call the current tab review
3. Please rename this coding tab to review.
4. Could you rename this coding tab to review?
5. Rename this coding tab to review, please.
6. I need you to rename this coding tab to review.
7. Please call the current tab review.
8. Could you call the current tab review?
9. Call the current tab review, please.
10. I need you to call the current tab review.

### `coding.workspace.close` (review needed)

1. Close this coding workspace
2. Shut the current coding workspace
3. Please close this coding workspace.
4. Could you close this coding workspace?
5. Close this coding workspace, please.
6. I need you to close this coding workspace.
7. Please shut the current coding workspace.
8. Could you shut the current coding workspace?
9. Shut the current coding workspace, please.
10. I need you to shut the current coding workspace.

### `coding.workspace.create` (review needed)

1. Create a coding workspace for the app
2. Start a new coding workspace for the app
3. Please create a coding workspace for the app.
4. Could you create a coding workspace for the app?
5. Create a coding workspace for the app, please.
6. I need you to create a coding workspace for the app.
7. Please start a new coding workspace for the app.
8. Could you start a new coding workspace for the app?
9. Start a new coding workspace for the app, please.
10. I need you to start a new coding workspace for the app.

### `coding.workspace.focus` (review needed)

1. Focus the app coding workspace
2. Switch to the app workspace
3. Please focus the app coding workspace.
4. Could you focus the app coding workspace?
5. Focus the app coding workspace, please.
6. I need you to focus the app coding workspace.
7. Please switch to the app workspace.
8. Could you switch to the app workspace?
9. Switch to the app workspace, please.
10. I need you to switch to the app workspace.

### `coding.workspace.get` (review needed)

1. Show details for the app workspace
2. Get information about this coding workspace
3. Please show details for the app workspace.
4. Could you show details for the app workspace?
5. Show details for the app workspace, please.
6. I need you to show details for the app workspace.
7. Please get information about this coding workspace.
8. Could you get information about this coding workspace?
9. Get information about this coding workspace, please.
10. I need you to get information about this coding workspace.

### `coding.workspace.list` (review needed)

1. List coding workspaces
2. Which coding workspaces are available?
3. Please list coding workspaces.
4. Could you list coding workspaces?
5. List coding workspaces, please.
6. I need you to list coding workspaces.
7. Please show the available coding workspaces.
8. Could you show the available coding workspaces?
9. Show the available coding workspaces, please.
10. I need you to show the available coding workspaces.

### `coding.workspace.rename` (review needed)

1. Rename this coding workspace to app
2. Call this workspace app
3. Please rename this coding workspace to app.
4. Could you rename this coding workspace to app?
5. Rename this coding workspace to app, please.
6. I need you to rename this coding workspace to app.
7. Please call this workspace app.
8. Could you call this workspace app?
9. Call this workspace app, please.
10. I need you to call this workspace app.

### `coding.worktree.create` (review needed)

1. Create a worktree for the fix
2. Make a new worktree for this change
3. Please create a worktree for the fix.
4. Could you create a worktree for the fix?
5. Create a worktree for the fix, please.
6. I need you to create a worktree for the fix.
7. Please make a new worktree for this change.
8. Could you make a new worktree for this change?
9. Make a new worktree for this change, please.
10. I need you to make a new worktree for this change.

### `coding.worktree.list` (review needed)

1. List the worktrees
2. Which worktrees exist?
3. Please list the worktrees.
4. Could you list the worktrees?
5. List the worktrees, please.
6. I need you to list the worktrees.
7. Please show the existing worktrees.
8. Could you show the existing worktrees?
9. Show the existing worktrees, please.
10. I need you to show the existing worktrees.

### `coding.worktree.open` (review needed)

1. Open the fix worktree
2. Switch to that worktree
3. Please open the fix worktree.
4. Could you open the fix worktree?
5. Open the fix worktree, please.
6. I need you to open the fix worktree.
7. Please switch to that worktree.
8. Could you switch to that worktree?
9. Switch to that worktree, please.
10. I need you to switch to that worktree.

### `coding.worktree.remove` (review needed)

1. Remove the old worktree
2. Delete that worktree
3. Please remove the old worktree.
4. Could you remove the old worktree?
5. Remove the old worktree, please.
6. I need you to remove the old worktree.
7. Please delete that worktree.
8. Could you delete that worktree?
9. Delete that worktree, please.
10. I need you to delete that worktree.

## dictation

### `dictation.cancel` (review needed)

1. Cancel this dictation
2. Discard what I just dictated
3. Please cancel this dictation.
4. Could you cancel this dictation?
5. Cancel this dictation, please.
6. I need you to cancel this dictation.
7. Please discard what I just dictated.
8. Could you discard what I just dictated?
9. Discard what I just dictated, please.
10. I need you to discard what I just dictated.

### `dictation.capture` (review needed)

1. Capture my speech as text
2. Record this utterance for transcription
3. Please capture my speech as text.
4. Could you capture my speech as text?
5. Capture my speech as text, please.
6. I need you to capture my speech as text.
7. Please record this utterance for transcription.
8. Could you record this utterance for transcription?
9. Record this utterance for transcription, please.
10. I need you to record this utterance for transcription.

### `dictation.chat` (review needed)

1. Start voice chat
2. Open the dictation chat mode
3. Please start voice chat.
4. Could you start voice chat?
5. Start voice chat, please.
6. I need you to start voice chat.
7. Please open the dictation chat mode.
8. Could you open the dictation chat mode?
9. Open the dictation chat mode, please.
10. I need you to open the dictation chat mode.

### `dictation.history` (review needed)

1. Show my dictation history
2. List previous transcriptions
3. Please show my dictation history.
4. Could you show my dictation history?
5. Show my dictation history, please.
6. I need you to show my dictation history.
7. Please list previous transcriptions.
8. Could you list previous transcriptions?
9. List previous transcriptions, please.
10. I need you to list previous transcriptions.

### `dictation.history_paste` (review needed)

1. Paste the last dictation
2. Insert my previous transcription
3. Please paste the last dictation.
4. Could you paste the last dictation?
5. Paste the last dictation, please.
6. I need you to paste the last dictation.
7. Please insert my previous transcription.
8. Could you insert my previous transcription?
9. Insert my previous transcription, please.
10. I need you to insert my previous transcription.

### `dictation.output_set` (review needed)

1. Send dictation to the clipboard
2. Change the dictation output to clipboard
3. Please send dictation to the clipboard.
4. Could you send dictation to the clipboard?
5. Send dictation to the clipboard, please.
6. I need you to send dictation to the clipboard.
7. Please change the dictation output to clipboard.
8. Could you change the dictation output to clipboard?
9. Change the dictation output to clipboard, please.
10. I need you to change the dictation output to clipboard.

### `dictation.paste_keys_set` (review needed)

1. Use Control V to paste dictation
2. Set the dictation paste shortcut to Control V
3. Please use Control V to paste dictation.
4. Could you use Control V to paste dictation?
5. Use Control V to paste dictation, please.
6. I need you to use Control V to paste dictation.
7. Please set the dictation paste shortcut to Control V.
8. Could you set the dictation paste shortcut to Control V?
9. Set the dictation paste shortcut to Control V, please.
10. I need you to set the dictation paste shortcut to Control V.

### `dictation.restart` (review needed)

1. Restart dictation
2. Start the dictation service again
3. Please restart dictation.
4. Could you restart dictation?
5. Restart dictation, please.
6. I need you to restart dictation.
7. Please start the dictation service again.
8. Could you start the dictation service again?
9. Start the dictation service again, please.
10. I need you to start the dictation service again.

### `dictation.start` (review needed)

1. Start dictation
2. Begin transcribing my speech
3. Please start dictation.
4. Could you start dictation?
5. Start dictation, please.
6. I need you to start dictation.
7. Please begin transcribing my speech.
8. Could you begin transcribing my speech?
9. Begin transcribing my speech, please.
10. I need you to begin transcribing my speech.

### `dictation.status` (review needed)

1. Is dictation running?
2. Show the dictation status
3. Please tell me whether dictation is running.
4. Could you tell me whether dictation is running?
5. Tell me whether dictation is running, please.
6. I need you to tell me whether dictation is running.
7. Please show the dictation status.
8. Could you show the dictation status?
9. Show the dictation status, please.
10. I need you to show the dictation status.

### `dictation.stop` (review needed)

1. Stop dictation
2. End the current dictation
3. Please stop dictation.
4. Could you stop dictation?
5. Stop dictation, please.
6. I need you to stop dictation.
7. Please end the current dictation.
8. Could you end the current dictation?
9. End the current dictation, please.
10. I need you to end the current dictation.

### `dictation.submit` (review needed)

1. Submit this dictation
2. Send the transcribed text now
3. Please submit this dictation.
4. Could you submit this dictation?
5. Submit this dictation, please.
6. I need you to submit this dictation.
7. Please send the transcribed text now.
8. Could you send the transcribed text now?
9. Send the transcribed text now, please.
10. I need you to send the transcribed text now.

### `dictation.toggle` (review needed)

1. Toggle dictation
2. Switch dictation on or off
3. Please toggle dictation.
4. Could you toggle dictation?
5. Toggle dictation, please.
6. I need you to toggle dictation.
7. Please switch dictation on or off.
8. Could you switch dictation on or off?
9. Switch dictation on or off, please.
10. I need you to switch dictation on or off.

## display

### `display.brightness_down` (typed)

1. Decrease brightness
2. Dim the screen
3. Please decrease brightness.
4. Could you decrease brightness?
5. Decrease brightness, please.
6. I need you to decrease brightness.
7. Please dim the screen.
8. Could you dim the screen?
9. Dim the screen, please.
10. I need you to dim the screen.

### `display.brightness_set` (review needed)

1. Set brightness to 60 percent
2. Make the screen 60 percent bright
3. Please set brightness to 60 percent.
4. Could you set brightness to 60 percent?
5. Set brightness to 60 percent, please.
6. I need you to set brightness to 60 percent.
7. Please make the screen 60 percent bright.
8. Could you make the screen 60 percent bright?
9. Make the screen 60 percent bright, please.
10. I need you to make the screen 60 percent bright.

### `display.brightness_up` (typed)

1. Increase brightness
2. Make the screen brighter
3. Please increase brightness.
4. Could you increase brightness?
5. Increase brightness, please.
6. I need you to increase brightness.
7. Please make the screen brighter.
8. Could you make the screen brighter?
9. Make the screen brighter, please.
10. I need you to make the screen brighter.

## email

### `email.read` (review needed)

1. Read the latest email
2. Show me the newest message in my inbox
3. Please read the latest email.
4. Could you read the latest email?
5. Read the latest email, please.
6. I need you to read the latest email.
7. Please show me the newest message in my inbox.
8. Could you show me the newest message in my inbox?
9. Show me the newest message in my inbox, please.
10. I need you to show me the newest message in my inbox.

### `email.reply` (review needed)

1. Reply to Sam's email
2. Write a response to that message
3. Please reply to Sam's email.
4. Could you reply to Sam's email?
5. Reply to Sam's email, please.
6. I need you to reply to Sam's email.
7. Please write a response to that message.
8. Could you write a response to that message?
9. Write a response to that message, please.
10. I need you to write a response to that message.

### `email.search` (review needed)

1. Find emails from Sam
2. Search my mail for the invoice
3. Please find emails from Sam.
4. Could you find emails from Sam?
5. Find emails from Sam, please.
6. I need you to find emails from Sam.
7. Please search my mail for the invoice.
8. Could you search my mail for the invoice?
9. Search my mail for the invoice, please.
10. I need you to search my mail for the invoice.

### `email.send` (review needed)

1. Send an email to Sam
2. Email the report to Sam
3. Please send an email to Sam.
4. Could you send an email to Sam?
5. Send an email to Sam, please.
6. I need you to send an email to Sam.
7. Please email the report to Sam.
8. Could you email the report to Sam?
9. Email the report to Sam, please.
10. I need you to email the report to Sam.

## extension

### `extension.failure_report` (review needed)

1. Show extension failures
2. Report which extension commands failed
3. Please show extension failures.
4. Could you show extension failures?
5. Show extension failures, please.
6. I need you to show extension failures.
7. Please report which extension commands failed.
8. Could you report which extension commands failed?
9. Report which extension commands failed, please.
10. I need you to report which extension commands failed.

### `extension.ipc_call` (review needed)

1. Call the extension's status endpoint
2. Send a status request to the extension
3. Please call the extension's status endpoint.
4. Could you call the extension's status endpoint?
5. Call the extension's status endpoint, please.
6. I need you to call the extension's status endpoint.
7. Please send a status request to the extension.
8. Could you send a status request to the extension?
9. Send a status request to the extension, please.
10. I need you to send a status request to the extension.

### `extension.script_run` (review needed)

1. Run the configured extension script
2. Execute the extension action
3. Please run the configured extension script.
4. Could you run the configured extension script?
5. Run the configured extension script, please.
6. I need you to run the configured extension script.
7. Please execute the extension action.
8. Could you execute the extension action?
9. Execute the extension action, please.
10. I need you to execute the extension action.

## file

### `file.list` (review needed)

1. List files in Downloads
2. Show what is in my Downloads folder
3. Please list files in Downloads.
4. Could you list files in Downloads?
5. List files in Downloads, please.
6. I need you to list files in Downloads.
7. Please show what is in my Downloads folder.
8. Could you show what is in my Downloads folder?
9. Show what is in my Downloads folder, please.
10. I need you to show what is in my Downloads folder.

### `file.open` (review needed)

1. Open the report file
2. Launch the selected document
3. Please open the report file.
4. Could you open the report file?
5. Open the report file, please.
6. I need you to open the report file.
7. Please launch the selected document.
8. Could you launch the selected document?
9. Launch the selected document, please.
10. I need you to launch the selected document.

### `file.read` (review needed)

1. Read the report file
2. Show the contents of that document
3. Please read the report file.
4. Could you read the report file?
5. Read the report file, please.
6. I need you to read the report file.
7. Please show the contents of that document.
8. Could you show the contents of that document?
9. Show the contents of that document, please.
10. I need you to show the contents of that document.

### `file.search` (review needed)

1. Find files named report
2. Search for the report document
3. Please find files named report.
4. Could you find files named report?
5. Find files named report, please.
6. I need you to find files named report.
7. Please search for the report document.
8. Could you search for the report document?
9. Search for the report document, please.
10. I need you to search for the report document.

## input

### `input.keypress` (review needed)

1. Press Control S
2. Send the Escape key
3. Please press Control S.
4. Could you press Control S?
5. Press Control S, please.
6. I need you to press Control S.
7. Please send the Escape key.
8. Could you send the Escape key?
9. Send the Escape key, please.
10. I need you to send the Escape key.

### `input.type_text` (review needed)

1. Type hello world
2. Enter the words hello world
3. Please type hello world.
4. Could you type hello world?
5. Type hello world, please.
6. I need you to type hello world.
7. Please enter the words hello world.
8. Could you enter the words hello world?
9. Enter the words hello world, please.
10. I need you to enter the words hello world.

## media

### `media.next` (typed)

1. Next track
2. Skip this song
3. Please skip to the next track.
4. Could you skip to the next track?
5. Skip to the next track, please.
6. I need you to skip to the next track.
7. Please skip this song.
8. Could you skip this song?
9. Skip this song, please.
10. I need you to skip this song.

### `media.pause` (typed)

1. Pause music
2. Stop playback
3. Please pause music.
4. Could you pause music?
5. Pause music, please.
6. I need you to pause music.
7. Please stop playback.
8. Could you stop playback?
9. Stop playback, please.
10. I need you to stop playback.

### `media.play` (typed)

1. Play music
2. Resume playback
3. Please play music.
4. Could you play music?
5. Play music, please.
6. I need you to play music.
7. Please resume playback.
8. Could you resume playback?
9. Resume playback, please.
10. I need you to resume playback.

### `media.play_pause` (review needed)

1. Toggle playback
2. Switch between play and pause
3. Please toggle playback.
4. Could you toggle playback?
5. Toggle playback, please.
6. I need you to toggle playback.
7. Please switch between play and pause.
8. Could you switch between play and pause?
9. Switch between play and pause, please.
10. I need you to switch between play and pause.

### `media.previous` (typed)

1. Previous track
2. Go back a track
3. Please go to the previous track.
4. Could you go to the previous track?
5. Go to the previous track, please.
6. I need you to go to the previous track.
7. Please go back a track.
8. Could you go back a track?
9. Go back a track, please.
10. I need you to go back a track.

## meeting

### `meeting.delete` (review needed)

1. Delete yesterday's meeting recording
2. Remove that saved meeting
3. Please delete yesterday's meeting recording.
4. Could you delete yesterday's meeting recording?
5. Delete yesterday's meeting recording, please.
6. I need you to delete yesterday's meeting recording.
7. Please remove that saved meeting.
8. Could you remove that saved meeting?
9. Remove that saved meeting, please.
10. I need you to remove that saved meeting.

### `meeting.export` (review needed)

1. Export the meeting transcript
2. Save a copy of the meeting notes
3. Please export the meeting transcript.
4. Could you export the meeting transcript?
5. Export the meeting transcript, please.
6. I need you to export the meeting transcript.
7. Please save a copy of the meeting notes.
8. Could you save a copy of the meeting notes?
9. Save a copy of the meeting notes, please.
10. I need you to save a copy of the meeting notes.

### `meeting.join` (review needed)

1. Join the team meeting
2. Enter the current meeting
3. Please join the team meeting.
4. Could you join the team meeting?
5. Join the team meeting, please.
6. I need you to join the team meeting.
7. Please enter the current meeting.
8. Could you enter the current meeting?
9. Enter the current meeting, please.
10. I need you to enter the current meeting.

### `meeting.label` (review needed)

1. Label this meeting weekly sync
2. Name the recording weekly sync
3. Please label this meeting weekly sync.
4. Could you label this meeting weekly sync?
5. Label this meeting weekly sync, please.
6. I need you to label this meeting weekly sync.
7. Please name the recording weekly sync.
8. Could you name the recording weekly sync?
9. Name the recording weekly sync, please.
10. I need you to name the recording weekly sync.

### `meeting.list` (review needed)

1. List my meetings
2. Show the saved meeting sessions
3. Please list my meetings.
4. Could you list my meetings?
5. List my meetings, please.
6. I need you to list my meetings.
7. Please show the saved meeting sessions.
8. Could you show the saved meeting sessions?
9. Show the saved meeting sessions, please.
10. I need you to show the saved meeting sessions.

### `meeting.pause` (review needed)

1. Pause meeting capture
2. Temporarily stop recording the meeting
3. Please pause meeting capture.
4. Could you pause meeting capture?
5. Pause meeting capture, please.
6. I need you to pause meeting capture.
7. Please temporarily stop recording the meeting.
8. Could you temporarily stop recording the meeting?
9. Temporarily stop recording the meeting, please.
10. I need you to temporarily stop recording the meeting.

### `meeting.resume` (review needed)

1. Resume meeting capture
2. Continue recording the meeting
3. Please resume meeting capture.
4. Could you resume meeting capture?
5. Resume meeting capture, please.
6. I need you to resume meeting capture.
7. Please continue recording the meeting.
8. Could you continue recording the meeting?
9. Continue recording the meeting, please.
10. I need you to continue recording the meeting.

### `meeting.show` (review needed)

1. Show the weekly sync meeting
2. Open that meeting's details
3. Please show the weekly sync meeting.
4. Could you show the weekly sync meeting?
5. Show the weekly sync meeting, please.
6. I need you to show the weekly sync meeting.
7. Please open that meeting's details.
8. Could you open that meeting's details?
9. Open that meeting's details, please.
10. I need you to open that meeting's details.

### `meeting.start` (review needed)

1. Start meeting capture
2. Begin recording this meeting
3. Please start meeting capture.
4. Could you start meeting capture?
5. Start meeting capture, please.
6. I need you to start meeting capture.
7. Please begin recording this meeting.
8. Could you begin recording this meeting?
9. Begin recording this meeting, please.
10. I need you to begin recording this meeting.

### `meeting.status` (review needed)

1. Is the meeting recorder running?
2. Show meeting capture status
3. Please tell me whether meeting capture is running.
4. Could you tell me whether meeting capture is running?
5. Tell me whether meeting capture is running, please.
6. I need you to tell me whether meeting capture is running.
7. Please show meeting capture status.
8. Could you show meeting capture status?
9. Show meeting capture status, please.
10. I need you to show meeting capture status.

### `meeting.stop` (review needed)

1. Stop meeting capture
2. Finish recording this meeting
3. Please stop meeting capture.
4. Could you stop meeting capture?
5. Stop meeting capture, please.
6. I need you to stop meeting capture.
7. Please finish recording this meeting.
8. Could you finish recording this meeting?
9. Finish recording this meeting, please.
10. I need you to finish recording this meeting.

### `meeting.summarize` (review needed)

1. Summarize the meeting
2. Give me a recap of that meeting
3. Please summarize the meeting.
4. Could you summarize the meeting?
5. Summarize the meeting, please.
6. I need you to summarize the meeting.
7. Please give me a recap of that meeting.
8. Could you give me a recap of that meeting?
9. Give me a recap of that meeting, please.
10. I need you to give me a recap of that meeting.

## message

### `message.send` (review needed)

1. Send Sam a message
2. Message Sam about the meeting
3. Please send Sam a message.
4. Could you send Sam a message?
5. Send Sam a message, please.
6. I need you to send Sam a message.
7. Please message Sam about the meeting.
8. Could you message Sam about the meeting?
9. Message Sam about the meeting, please.
10. I need you to message Sam about the meeting.

## network

### `network.connect_open` (review needed)

1. Connect to the guest Wi-Fi
2. Join the open guest network
3. Please connect to the guest Wi-Fi.
4. Could you connect to the guest Wi-Fi?
5. Connect to the guest Wi-Fi, please.
6. I need you to connect to the guest Wi-Fi.
7. Please join the open guest network.
8. Could you join the open guest network?
9. Join the open guest network, please.
10. I need you to join the open guest network.

### `network.connect_saved` (review needed)

1. Connect to my saved home Wi-Fi
2. Join the remembered home network
3. Please connect to my saved home Wi-Fi.
4. Could you connect to my saved home Wi-Fi?
5. Connect to my saved home Wi-Fi, please.
6. I need you to connect to my saved home Wi-Fi.
7. Please join the remembered home network.
8. Could you join the remembered home network?
9. Join the remembered home network, please.
10. I need you to join the remembered home network.

### `network.disconnect` (review needed)

1. Disconnect from Wi-Fi
2. Leave the current wireless network
3. Please disconnect from Wi-Fi.
4. Could you disconnect from Wi-Fi?
5. Disconnect from Wi-Fi, please.
6. I need you to disconnect from Wi-Fi.
7. Please leave the current wireless network.
8. Could you leave the current wireless network?
9. Leave the current wireless network, please.
10. I need you to leave the current wireless network.

### `network.wifi_disable` (review needed)

1. Turn off Wi-Fi
2. Disable the wireless adapter
3. Please turn off Wi-Fi.
4. Could you turn off Wi-Fi?
5. Turn off Wi-Fi, please.
6. I need you to turn off Wi-Fi.
7. Please disable the wireless adapter.
8. Could you disable the wireless adapter?
9. Disable the wireless adapter, please.
10. I need you to disable the wireless adapter.

### `network.wifi_enable` (review needed)

1. Turn on Wi-Fi
2. Enable the wireless adapter
3. Please turn on Wi-Fi.
4. Could you turn on Wi-Fi?
5. Turn on Wi-Fi, please.
6. I need you to turn on Wi-Fi.
7. Please enable the wireless adapter.
8. Could you enable the wireless adapter?
9. Enable the wireless adapter, please.
10. I need you to enable the wireless adapter.

## notes

### `notes.remember` (typed)

1. Remember that the server is on port 8080
2. Save this note
3. Please remember that the server is on port 8080.
4. Could you remember that the server is on port 8080?
5. Remember that the server is on port 8080, please.
6. I need you to remember that the server is on port 8080.
7. Please save this note.
8. Could you save this note?
9. Save this note, please.
10. I need you to save this note.

## project

### `project.comment` (review needed)

1. Comment on this project item
2. Add a note to the current project task
3. Please comment on this project item.
4. Could you comment on this project item?
5. Comment on this project item, please.
6. I need you to comment on this project item.
7. Please add a note to the current project task.
8. Could you add a note to the current project task?
9. Add a note to the current project task, please.
10. I need you to add a note to the current project task.

### `project.list` (review needed)

1. List my projects
2. Which projects do I have?
3. Please list my projects.
4. Could you list my projects?
5. List my projects, please.
6. I need you to list my projects.
7. Please show my projects.
8. Could you show my projects?
9. Show my projects, please.
10. I need you to show my projects.

### `project.search` (review needed)

1. Find the website project
2. Search my projects for the website
3. Please find the website project.
4. Could you find the website project?
5. Find the website project, please.
6. I need you to find the website project.
7. Please search my projects for the website.
8. Could you search my projects for the website?
9. Search my projects for the website, please.
10. I need you to search my projects for the website.

### `project.todo_create` (review needed)

1. Add a project to-do to review the design
2. Create a project task for the design review
3. Please add a project to-do to review the design.
4. Could you add a project to-do to review the design?
5. Add a project to-do to review the design, please.
6. I need you to add a project to-do to review the design.
7. Please create a project task for the design review.
8. Could you create a project task for the design review?
9. Create a project task for the design review, please.
10. I need you to create a project task for the design review.

### `project.todo_list` (review needed)

1. Show the project to-dos
2. List tasks in this project
3. Please show the project to-dos.
4. Could you show the project to-dos?
5. Show the project to-dos, please.
6. I need you to show the project to-dos.
7. Please list tasks in this project.
8. Could you list tasks in this project?
9. List tasks in this project, please.
10. I need you to list tasks in this project.

## reminder

### `reminder.create` (typed)

1. Remind me in ten minutes to stretch
2. Set a reminder to call Alex
3. Please remind me in ten minutes to stretch.
4. Could you remind me in ten minutes to stretch?
5. Remind me in ten minutes to stretch, please.
6. I need you to remind me in ten minutes to stretch.
7. Please set a reminder to call Alex.
8. Could you set a reminder to call Alex?
9. Set a reminder to call Alex, please.
10. I need you to set a reminder to call Alex.

## routine

### `routine.schedule` (review needed)

1. Schedule the morning routine for eight
2. Run my morning routine at eight
3. Please schedule the morning routine for eight.
4. Could you schedule the morning routine for eight?
5. Schedule the morning routine for eight, please.
6. I need you to schedule the morning routine for eight.
7. Please run my morning routine at eight.
8. Could you run my morning routine at eight?
9. Run my morning routine at eight, please.
10. I need you to run my morning routine at eight.

## screen

### `screen.click_text` (review needed)

1. Click the text that says Continue
2. Select the Continue label on screen
3. Please click the text that says Continue.
4. Could you click the text that says Continue?
5. Click the text that says Continue, please.
6. I need you to click the text that says Continue.
7. Please select the Continue label on screen.
8. Could you select the Continue label on screen?
9. Select the Continue label on screen, please.
10. I need you to select the Continue label on screen.

### `screen.read` (typed)

1. What is on my screen?
2. Read the visible window
3. Please tell me what is on my screen.
4. Could you tell me what is on my screen?
5. Tell me what is on my screen, please.
6. I need you to tell me what is on my screen.
7. Please read the visible window.
8. Could you read the visible window?
9. Read the visible window, please.
10. I need you to read the visible window.

## smarthome

### `smarthome.device_set` (typed)

1. Turn off the living room lights
2. Switch on the fan
3. Please turn off the living room lights.
4. Could you turn off the living room lights?
5. Turn off the living room lights, please.
6. I need you to turn off the living room lights.
7. Please switch on the fan.
8. Could you switch on the fan?
9. Switch on the fan, please.
10. I need you to switch on the fan.

### `smarthome.device_toggle` (review needed)

1. Toggle the kitchen lights
2. Switch the kitchen lights on or off
3. Please toggle the kitchen lights.
4. Could you toggle the kitchen lights?
5. Toggle the kitchen lights, please.
6. I need you to toggle the kitchen lights.
7. Please switch the kitchen lights on or off.
8. Could you switch the kitchen lights on or off?
9. Switch the kitchen lights on or off, please.
10. I need you to switch the kitchen lights on or off.

### `smarthome.scene_activate` (review needed)

1. Activate movie night
2. Turn on the movie night scene
3. Please activate movie night.
4. Could you activate movie night?
5. Activate movie night, please.
6. I need you to activate movie night.
7. Please turn on the movie night scene.
8. Could you turn on the movie night scene?
9. Turn on the movie night scene, please.
10. I need you to turn on the movie night scene.

## speech

### `speech.backend_set` (review needed)

1. Use the local speech backend
2. Change speech output to the local backend
3. Please use the local speech backend.
4. Could you use the local speech backend?
5. Use the local speech backend, please.
6. I need you to use the local speech backend.
7. Please change speech output to the local backend.
8. Could you change speech output to the local backend?
9. Change speech output to the local backend, please.
10. I need you to change speech output to the local backend.

### `speech.correction_save` (review needed)

1. Remember that transcription correction
2. Save my correction for that word
3. Please remember that transcription correction.
4. Could you remember that transcription correction?
5. Remember that transcription correction, please.
6. I need you to remember that transcription correction.
7. Please save my correction for that word.
8. Could you save my correction for that word?
9. Save my correction for that word, please.
10. I need you to save my correction for that word.

### `speech.engine_set` (review needed)

1. Use the Whisper speech engine
2. Switch speech recognition to Whisper
3. Please use the Whisper speech engine.
4. Could you use the Whisper speech engine?
5. Use the Whisper speech engine, please.
6. I need you to use the Whisper speech engine.
7. Please switch speech recognition to Whisper.
8. Could you switch speech recognition to Whisper?
9. Switch speech recognition to Whisper, please.
10. I need you to switch speech recognition to Whisper.

### `speech.language_set` (review needed)

1. Set speech language to English
2. Use English for speech recognition
3. Please set speech language to English.
4. Could you set speech language to English?
5. Set speech language to English, please.
6. I need you to set speech language to English.
7. Please use English for speech recognition.
8. Could you use English for speech recognition?
9. Use English for speech recognition, please.
10. I need you to use English for speech recognition.

### `speech.model_install` (review needed)

1. Install the small speech model
2. Download the small transcription model
3. Please install the small speech model.
4. Could you install the small speech model?
5. Install the small speech model, please.
6. I need you to install the small speech model.
7. Please download the small transcription model.
8. Could you download the small transcription model?
9. Download the small transcription model, please.
10. I need you to download the small transcription model.

### `speech.read_screen` (review needed)

1. Read the screen aloud
2. Speak what is on screen
3. Please read the screen aloud.
4. Could you read the screen aloud?
5. Read the screen aloud, please.
6. I need you to read the screen aloud.
7. Please speak what is on screen.
8. Could you speak what is on screen?
9. Speak what is on screen, please.
10. I need you to speak what is on screen.

### `speech.read_selection` (review needed)

1. Read the selected text aloud
2. Speak my current selection
3. Please read the selected text aloud.
4. Could you read the selected text aloud?
5. Read the selected text aloud, please.
6. I need you to read the selected text aloud.
7. Please speak my current selection.
8. Could you speak my current selection?
9. Speak my current selection, please.
10. I need you to speak my current selection.

### `speech.route` (review needed)

1. Send speech output to the headphones
2. Route spoken audio to the headset
3. Please send speech output to the headphones.
4. Could you send speech output to the headphones?
5. Send speech output to the headphones, please.
6. I need you to send speech output to the headphones.
7. Please route spoken audio to the headset.
8. Could you route spoken audio to the headset?
9. Route spoken audio to the headset, please.
10. I need you to route spoken audio to the headset.

### `speech.say` (typed)

1. Say hello
2. Speak the current time
3. Please say hello.
4. Could you say hello?
5. Say hello, please.
6. I need you to say hello.
7. Please speak the current time.
8. Could you speak the current time?
9. Speak the current time, please.
10. I need you to speak the current time.

### `speech.speed_set` (review needed)

1. Set speech speed to 1.2 times
2. Speak twenty percent faster
3. Please set speech speed to 1.2 times.
4. Could you set speech speed to 1.2 times?
5. Set speech speed to 1.2 times, please.
6. I need you to set speech speed to 1.2 times.
7. Please speak twenty percent faster.
8. Could you speak twenty percent faster?
9. Speak twenty percent faster, please.
10. I need you to speak twenty percent faster.

### `speech.stop` (review needed)

1. Stop speaking
2. Silence the current speech output
3. Please stop speaking.
4. Could you stop speaking?
5. Stop speaking, please.
6. I need you to stop speaking.
7. Please silence the current speech output.
8. Could you silence the current speech output?
9. Silence the current speech output, please.
10. I need you to silence the current speech output.

### `speech.transcribe_file` (review needed)

1. Transcribe the interview file
2. Turn that audio file into text
3. Please transcribe the interview file.
4. Could you transcribe the interview file?
5. Transcribe the interview file, please.
6. I need you to transcribe the interview file.
7. Please turn that audio file into text.
8. Could you turn that audio file into text?
9. Turn that audio file into text, please.
10. I need you to turn that audio file into text.

### `speech.vocabulary_query` (review needed)

1. Show my speech vocabulary
2. Which custom words do you know?
3. Please show my speech vocabulary.
4. Could you show my speech vocabulary?
5. Show my speech vocabulary, please.
6. I need you to show my speech vocabulary.
7. Please show the custom speech words.
8. Could you show the custom speech words?
9. Show the custom speech words, please.
10. I need you to show the custom speech words.

### `speech.voice_install` (review needed)

1. Install the Alex voice
2. Download the Alex speech voice
3. Please install the Alex voice.
4. Could you install the Alex voice?
5. Install the Alex voice, please.
6. I need you to install the Alex voice.
7. Please download the Alex speech voice.
8. Could you download the Alex speech voice?
9. Download the Alex speech voice, please.
10. I need you to download the Alex speech voice.

### `speech.voice_select` (review needed)

1. Select the Alex voice
2. Speak with the Alex voice
3. Please select the Alex voice.
4. Could you select the Alex voice?
5. Select the Alex voice, please.
6. I need you to select the Alex voice.
7. Please speak with the Alex voice.
8. Could you speak with the Alex voice?
9. Speak with the Alex voice, please.
10. I need you to speak with the Alex voice.

## system

### `system.battery_query` (typed)

1. How much battery is left?
2. Tell me the battery level
3. Please tell me how much battery is left.
4. Could you tell me how much battery is left?
5. Tell me how much battery is left, please.
6. I need you to tell me how much battery is left.
7. Please tell me the battery level.
8. Could you tell me the battery level?
9. Tell me the battery level, please.
10. I need you to tell me the battery level.

### `system.idle_set` (review needed)

1. Set idle timeout to ten minutes
2. Make the computer idle after ten minutes
3. Please set idle timeout to ten minutes.
4. Could you set idle timeout to ten minutes?
5. Set idle timeout to ten minutes, please.
6. I need you to set idle timeout to ten minutes.
7. Please make the computer idle after ten minutes.
8. Could you make the computer idle after ten minutes?
9. Make the computer idle after ten minutes, please.
10. I need you to make the computer idle after ten minutes.

### `system.idle_toggle` (review needed)

1. Toggle idle handling
2. Switch the idle service on or off
3. Please toggle idle handling.
4. Could you toggle idle handling?
5. Toggle idle handling, please.
6. I need you to toggle idle handling.
7. Please switch the idle service on or off.
8. Could you switch the idle service on or off?
9. Switch the idle service on or off, please.
10. I need you to switch the idle service on or off.

### `system.lock` (typed)

1. Lock the screen
2. Lock my computer
3. Please lock the screen.
4. Could you lock the screen?
5. Lock the screen, please.
6. I need you to lock the screen.
7. Please lock my computer.
8. Could you lock my computer?
9. Lock my computer, please.
10. I need you to lock my computer.

### `system.logout` (review needed)

1. Log me out
2. End my desktop session
3. Please log me out.
4. Could you log me out?
5. Log me out, please.
6. I need you to log me out.
7. Please end my desktop session.
8. Could you end my desktop session?
9. End my desktop session, please.
10. I need you to end my desktop session.

### `system.menu_open` (review needed)

1. Open the system menu
2. Show the Omarchy menu
3. Please open the system menu.
4. Could you open the system menu?
5. Open the system menu, please.
6. I need you to open the system menu.
7. Please show the Omarchy menu.
8. Could you show the Omarchy menu?
9. Show the Omarchy menu, please.
10. I need you to show the Omarchy menu.

### `system.nightlight_toggle` (review needed)

1. Toggle night light
2. Switch the warm screen filter on or off
3. Please toggle night light.
4. Could you toggle night light?
5. Toggle night light, please.
6. I need you to toggle night light.
7. Please switch the warm screen filter on or off.
8. Could you switch the warm screen filter on or off?
9. Switch the warm screen filter on or off, please.
10. I need you to switch the warm screen filter on or off.

### `system.notifications_silence_toggle` (review needed)

1. Toggle do not disturb
2. Switch notification sounds on or off
3. Please toggle do not disturb.
4. Could you toggle do not disturb?
5. Toggle do not disturb, please.
6. I need you to toggle do not disturb.
7. Please switch notification sounds on or off.
8. Could you switch notification sounds on or off?
9. Switch notification sounds on or off, please.
10. I need you to switch notification sounds on or off.

### `system.panel_open` (review needed)

1. Open the system panel
2. Show the control panel
3. Please open the system panel.
4. Could you open the system panel?
5. Open the system panel, please.
6. I need you to open the system panel.
7. Please show the control panel.
8. Could you show the control panel?
9. Show the control panel, please.
10. I need you to show the control panel.

### `system.power_profile_set` (typed)

1. Set power mode to performance
2. Use power saver
3. Please set power mode to performance.
4. Could you set power mode to performance?
5. Set power mode to performance, please.
6. I need you to set power mode to performance.
7. Please use power saver.
8. Could you use power saver?
9. Use power saver, please.
10. I need you to use power saver.

### `system.reboot` (typed)

1. Restart the computer
2. Reboot the machine
3. Please restart the computer.
4. Could you restart the computer?
5. Restart the computer, please.
6. I need you to restart the computer.
7. Please reboot the machine.
8. Could you reboot the machine?
9. Reboot the machine, please.
10. I need you to reboot the machine.

### `system.screenshot` (typed)

1. Take a screenshot
2. Capture the screen
3. Please take a screenshot.
4. Could you take a screenshot?
5. Take a screenshot, please.
6. I need you to take a screenshot.
7. Please capture the screen.
8. Could you capture the screen?
9. Capture the screen, please.
10. I need you to capture the screen.

### `system.shutdown` (typed)

1. Shut down the computer
2. Power off this machine
3. Please shut down the computer.
4. Could you shut down the computer?
5. Shut down the computer, please.
6. I need you to shut down the computer.
7. Please power off this machine.
8. Could you power off this machine?
9. Power off this machine, please.
10. I need you to power off this machine.

### `system.status_query` (review needed)

1. Show system status
2. How is my computer doing?
3. Please show system status.
4. Could you show system status?
5. Show system status, please.
6. I need you to show system status.
7. Please tell me how the computer is doing.
8. Could you tell me how the computer is doing?
9. Tell me how the computer is doing, please.
10. I need you to tell me how the computer is doing.

### `system.suspend` (typed)

1. Put the computer to sleep
2. Suspend the system
3. Please put the computer to sleep.
4. Could you put the computer to sleep?
5. Put the computer to sleep, please.
6. I need you to put the computer to sleep.
7. Please suspend the system.
8. Could you suspend the system?
9. Suspend the system, please.
10. I need you to suspend the system.

### `system.theme_set` (typed)

1. Switch theme to Tokyo Night
2. Apply the light theme
3. Please switch theme to Tokyo Night.
4. Could you switch theme to Tokyo Night?
5. Switch theme to Tokyo Night, please.
6. I need you to switch theme to Tokyo Night.
7. Please apply the light theme.
8. Could you apply the light theme?
9. Apply the light theme, please.
10. I need you to apply the light theme.

### `system.time_query` (typed)

1. What time is it?
2. Tell me the time
3. Please tell me the current time.
4. Could you tell me the current time?
5. Tell me the current time, please.
6. I need you to tell me the current time.
7. Please tell me the time.
8. Could you tell me the time?
9. Tell me the time, please.
10. I need you to tell me the time.

### `system.wait` (review needed)

1. Wait ten seconds
2. Pause for ten seconds
3. Please wait ten seconds.
4. Could you wait ten seconds?
5. Wait ten seconds, please.
6. I need you to wait ten seconds.
7. Please pause for ten seconds.
8. Could you pause for ten seconds?
9. Pause for ten seconds, please.
10. I need you to pause for ten seconds.

## task

### `task.cancel` (review needed)

1. Cancel task one
2. Stop that background task
3. Please cancel task one.
4. Could you cancel task one?
5. Cancel task one, please.
6. I need you to cancel task one.
7. Please stop that background task.
8. Could you stop that background task?
9. Stop that background task, please.
10. I need you to stop that background task.

### `task.list` (review needed)

1. List my tasks
2. Which tasks are running?
3. Please list my tasks.
4. Could you list my tasks?
5. List my tasks, please.
6. I need you to list my tasks.
7. Please show the running tasks.
8. Could you show the running tasks?
9. Show the running tasks, please.
10. I need you to show the running tasks.

### `task.read` (review needed)

1. Read task one's output
2. Show what that task produced
3. Please read task one's output.
4. Could you read task one's output?
5. Read task one's output, please.
6. I need you to read task one's output.
7. Please show what that task produced.
8. Could you show what that task produced?
9. Show what that task produced, please.
10. I need you to show what that task produced.

### `task.resume` (review needed)

1. Resume task one
2. Continue the paused task
3. Please resume task one.
4. Could you resume task one?
5. Resume task one, please.
6. I need you to resume task one.
7. Please continue the paused task.
8. Could you continue the paused task?
9. Continue the paused task, please.
10. I need you to continue the paused task.

### `task.status` (typed)

1. How is the coding task going?
2. Check the agent status
3. Please tell me how the coding task is going.
4. Could you tell me how the coding task is going?
5. Tell me how the coding task is going, please.
6. I need you to tell me how the coding task is going.
7. Please check the agent status.
8. Could you check the agent status?
9. Check the agent status, please.
10. I need you to check the agent status.

### `task.submit` (typed)

1. Start a coding task to fix the tests
2. Analyze this repository in the background
3. Please start a coding task to fix the tests.
4. Could you start a coding task to fix the tests?
5. Start a coding task to fix the tests, please.
6. I need you to start a coding task to fix the tests.
7. Please analyze this repository in the background.
8. Could you analyze this repository in the background?
9. Analyze this repository in the background, please.
10. I need you to analyze this repository in the background.

## terminal

### `terminal.list` (review needed)

1. List open terminals
2. Which terminal sessions exist?
3. Please list open terminals.
4. Could you list open terminals?
5. List open terminals, please.
6. I need you to list open terminals.
7. Please show the terminal sessions.
8. Could you show the terminal sessions?
9. Show the terminal sessions, please.
10. I need you to show the terminal sessions.

### `terminal.open` (review needed)

1. Open a terminal
2. Launch a new terminal window
3. Please open a terminal.
4. Could you open a terminal?
5. Open a terminal, please.
6. I need you to open a terminal.
7. Please launch a new terminal window.
8. Could you launch a new terminal window?
9. Launch a new terminal window, please.
10. I need you to launch a new terminal window.

### `terminal.read` (typed)

1. Read the terminal output
2. What does the build say?
3. Please read the terminal output.
4. Could you read the terminal output?
5. Read the terminal output, please.
6. I need you to read the terminal output.
7. Please tell me what the build says.
8. Could you tell me what the build says?
9. Tell me what the build says, please.
10. I need you to tell me what the build says.

### `terminal.run` (typed)

1. Run the tests in this terminal
2. Execute make build
3. Please run the tests in this terminal.
4. Could you run the tests in this terminal?
5. Run the tests in this terminal, please.
6. I need you to run the tests in this terminal.
7. Please execute make build.
8. Could you execute make build?
9. Execute make build, please.
10. I need you to execute make build.

### `terminal.watch` (typed)

1. Tell me when the build finishes
2. Notify me when this terminal is idle
3. Please tell me when the build finishes.
4. Could you tell me when the build finishes?
5. Tell me when the build finishes, please.
6. I need you to tell me when the build finishes.
7. Please notify me when this terminal is idle.
8. Could you notify me when this terminal is idle?
9. Notify me when this terminal is idle, please.
10. I need you to notify me when this terminal is idle.

## tv

### `tv.power_set` (typed)

1. Turn on the TV
2. Switch off the television
3. Please turn on the TV.
4. Could you turn on the TV?
5. Turn on the TV, please.
6. I need you to turn on the TV.
7. Please switch off the television.
8. Could you switch off the television?
9. Switch off the television, please.
10. I need you to switch off the television.

### `tv.remote_action` (review needed)

1. Press volume up on the TV remote
2. Send the TV a channel up command
3. Please press volume up on the TV remote.
4. Could you press volume up on the TV remote?
5. Press volume up on the TV remote, please.
6. I need you to press volume up on the TV remote.
7. Please send the TV a channel up command.
8. Could you send the TV a channel up command?
9. Send the TV a channel up command, please.
10. I need you to send the TV a channel up command.

## web

### `web.search` (review needed)

1. Search the web for Omarchy docs
2. Look online for Omarchy documentation
3. Please search the web for Omarchy docs.
4. Could you search the web for Omarchy docs?
5. Search the web for Omarchy docs, please.
6. I need you to search the web for Omarchy docs.
7. Please look online for Omarchy documentation.
8. Could you look online for Omarchy documentation?
9. Look online for Omarchy documentation, please.
10. I need you to look online for Omarchy documentation.

## window

### `window.close` (typed)

1. Close this window
2. Close the terminal
3. Please close this window.
4. Could you close this window?
5. Close this window, please.
6. I need you to close this window.
7. Please close the terminal.
8. Could you close the terminal?
9. Close the terminal, please.
10. I need you to close the terminal.

### `window.compose` (review needed)

1. Arrange these windows side by side
2. Put the windows into a layout
3. Please arrange these windows side by side.
4. Could you arrange these windows side by side?
5. Arrange these windows side by side, please.
6. I need you to arrange these windows side by side.
7. Please put the windows into a layout.
8. Could you put the windows into a layout?
9. Put the windows into a layout, please.
10. I need you to put the windows into a layout.

### `window.float` (typed)

1. Float this window
2. Make the active window tiled
3. Please float this window.
4. Could you float this window?
5. Float this window, please.
6. I need you to float this window.
7. Please make the active window tiled.
8. Could you make the active window tiled?
9. Make the active window tiled, please.
10. I need you to make the active window tiled.

### `window.focus` (typed)

1. Focus the terminal
2. Switch to the GitHub window
3. Please focus the terminal.
4. Could you focus the terminal?
5. Focus the terminal, please.
6. I need you to focus the terminal.
7. Please switch to the GitHub window.
8. Could you switch to the GitHub window?
9. Switch to the GitHub window, please.
10. I need you to switch to the GitHub window.

### `window.fullscreen` (typed)

1. Make this window fullscreen
2. Exit fullscreen
3. Please make this window fullscreen.
4. Could you make this window fullscreen?
5. Make this window fullscreen, please.
6. I need you to make this window fullscreen.
7. Please exit fullscreen.
8. Could you exit fullscreen?
9. Exit fullscreen, please.
10. I need you to exit fullscreen.

### `window.hide` (typed)

1. Hide this window
2. Hide all terminals
3. Please hide this window.
4. Could you hide this window?
5. Hide this window, please.
6. I need you to hide this window.
7. Please hide all terminals.
8. Could you hide all terminals?
9. Hide all terminals, please.
10. I need you to hide all terminals.

### `window.list` (typed)

1. List open windows
2. What windows are open?
3. Please list open windows.
4. Could you list open windows?
5. List open windows, please.
6. I need you to list open windows.
7. Please show the open windows.
8. Could you show the open windows?
9. Show the open windows, please.
10. I need you to show the open windows.

### `window.manage` (review needed)

1. Manage the focused window
2. Open controls for this window
3. Please manage the focused window.
4. Could you manage the focused window?
5. Manage the focused window, please.
6. I need you to manage the focused window.
7. Please open controls for this window.
8. Could you open controls for this window?
9. Open controls for this window, please.
10. I need you to open controls for this window.

### `window.maximize` (typed)

1. Maximize this window
2. Maximize Firefox
3. Please maximize this window.
4. Could you maximize this window?
5. Maximize this window, please.
6. I need you to maximize this window.
7. Please maximize Firefox.
8. Could you maximize Firefox?
9. Maximize Firefox, please.
10. I need you to maximize Firefox.

### `window.move_monitor` (typed)

1. Move this window to the other screen
2. Put Discord on the other monitor
3. Please move this window to the other screen.
4. Could you move this window to the other screen?
5. Move this window to the other screen, please.
6. I need you to move this window to the other screen.
7. Please put Discord on the other monitor.
8. Could you put Discord on the other monitor?
9. Put Discord on the other monitor, please.
10. I need you to put Discord on the other monitor.

### `window.tile` (typed)

1. Tile open windows
2. Tile the terminals
3. Please tile open windows.
4. Could you tile open windows?
5. Tile open windows, please.
6. I need you to tile open windows.
7. Please tile the terminals.
8. Could you tile the terminals?
9. Tile the terminals, please.
10. I need you to tile the terminals.

### `window.tile_pair` (review needed)

1. Tile this window with the browser
2. Put this window beside the browser
3. Please tile this window with the browser.
4. Could you tile this window with the browser?
5. Tile this window with the browser, please.
6. I need you to tile this window with the browser.
7. Please put this window beside the browser.
8. Could you put this window beside the browser?
9. Put this window beside the browser, please.
10. I need you to put this window beside the browser.

## workspace

### `workspace.manage` (review needed)

1. Manage this workspace
2. Open controls for the current workspace
3. Please manage this workspace.
4. Could you manage this workspace?
5. Manage this workspace, please.
6. I need you to manage this workspace.
7. Please open controls for the current workspace.
8. Could you open controls for the current workspace?
9. Open controls for the current workspace, please.
10. I need you to open controls for the current workspace.

### `workspace.move_window` (typed)

1. Move this window to workspace 3
2. Send Firefox to workspace 2
3. Please move this window to workspace 3.
4. Could you move this window to workspace 3?
5. Move this window to workspace 3, please.
6. I need you to move this window to workspace 3.
7. Please send Firefox to workspace 2.
8. Could you send Firefox to workspace 2?
9. Send Firefox to workspace 2, please.
10. I need you to send Firefox to workspace 2.

### `workspace.switch` (typed)

1. Go to workspace 2
2. Switch to workspace 4
3. Please go to workspace 2.
4. Could you go to workspace 2?
5. Go to workspace 2, please.
6. I need you to go to workspace 2.
7. Please switch to workspace 4.
8. Could you switch to workspace 4?
9. Switch to workspace 4, please.
10. I need you to switch to workspace 4.
