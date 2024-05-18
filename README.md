# eassay-writer

4. The application will open in your default web browser.
5. Enter the essay topic in the provided input field.
6. Specify the desired number of words for the essay.
7. Select the target audience (essay style) from the dropdown menu.
8. Click the "Write" button to generate the essay.
9. The generated essay will be displayed on the web page.

## Code Structure

The main components of the code are:

- `LLamaFunction`: This function takes the essay topic, desired number of words, and essay style as input. It loads the LLama 2 model, creates a prompt template, formats the prompt with the provided inputs, and generates the essay response using the LLama 2 model.
- Streamlit app: The Streamlit application sets up the user interface, including input fields for the essay topic, number of words, and essay style. It also handles the submission of the form and displays the generated essay response.

## Customization

You can customize the application by modifying the following aspects:

- Prompt template: Adjust the prompt template in the `LLamaFunction` to change the instructions given to the language model.
- Model configuration: Modify the model configuration in the `CTransformers` initialization to adjust parameters like temperature or maximum token length.
- User interface: Modify the Streamlit app code to change the layout, styling, or add additional features to the user interface.

## Note

Running the LLama 2 model requires significant computational resources and memory. Ensure that you have the necessary hardware and resources available before running the application.
