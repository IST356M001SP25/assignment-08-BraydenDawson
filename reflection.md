# Reflection

Student Name:  Brayden Dawson
Sudent Email:  bcdawson@syr.edu

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

**Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 

**Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`
In this assignment, I deepened my understanding of ETL processes and how they directly support data visualization. Specifically, I practiced extracting data from a source file, transforming it using pandas groupby and filtering techniques, and loading the results into new CSV files for use in Streamlit dashboards. One area I struggled with was making sure my output DataFrames matched the expected column names and counts for the test cases. For example, I had an issue where I used the column name hour instead of hourofday, which caused one of the tests to fail. This taught me the importance of paying close attention to schema and naming conventions when working with structured data.

On the dashboard side, I gained experience building interactive visualizations with Streamlit, including metrics, bar charts, line charts, and embedded maps using Folium. One challenge was scaling the circle markers on the map based on fine amounts — I had to write a custom scaling function to ensure the markers were visually proportional and informative. I also learned how to use layout elements like st.columns() to make the dashboard more readable.

Overall, this assignment helped me connect the dots between raw data and end-user visualization. I feel more confident working with pandas for transformation tasks, and I want to continue practicing Streamlit to create more user-friendly dashboards. In the future, I’d like to explore more advanced interactive components, like multi-filters or time sliders, to make dashboards even more dynamic.
