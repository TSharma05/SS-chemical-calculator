# Chemical Calculator: Coding Challenge


**Step 1: Turned the shared products in to lists of dictionaries**
 - Allows me to access specific parts of the products that are needed for the calculations
 - I added in number of peroxyl groups and molecular mass since those will both be needed for the calculations. This information was found at pubchem.

**Step 2: Create function that determines percent of hydrogen peroxide**
- First need to check if hydrogen peroxide is an ingredient in the product by iterating over the dictionary of chemicals for each product
- If hydrogen peroxide is present then use the max concentration of the hydrogen peroxide and divide by the total concentration of the product
- Multiply by 100 to make this a percent

**Step 3: Create function to calculate avaialble oxygen content (O<sub>a</sub>)**
- Loop through the products dictionaries and assign variables for the peroxy groups, max concentration, and molecular mass. This is for ease of calculations
- Multiple the number of peroxy groups by the max concentration then divide by the molecular mass
- This will be completed for each chemical in the product and added to a total sum. That sum is then multiplied by 16, this is the available oxygen content for that product