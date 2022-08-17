# Phoenix Suns Adoption of NFT's
<br>![1 0](https://user-images.githubusercontent.com/98990090/185028051-0ced8559-3933-41c8-931c-861be9b165b2.png)

Project created by Rachel Carroll, Joseph Garcia, Matt Pretel

## Background:
We are wanting to create a pitch to the Phoenix Suns to adopt NFT's into their revenue stream using different ticket packages. The NBA has reached an all time low for ticket revenue in 2021 since 2012 - the majority of the NBA's revenue stream comes from advertising, merchandising partnerships (like Adidas), and television contracts. We are also hoping to increase season long loyalty with added benefits like discounts on merchandise. We built a contract using Remix and connected through MetaMask and Ganache for purchasing via a D'app on Streamlit.

Packages available for purchase through the application:<br>
* **Standard Package:** Game ticket, NFT, and 5% off Merchandise for the Season<br>
* **Ultra Package:** Game ticket, $40 F&B Package, NFT, and 10% off Merchandise for the Season<br>
* **VIP Package:** Game ticket, $$100 F&B Package, Signed Photo with Suns Team, NFT, and 15% off Merchandise for the Season<br>

## Libaries Used:<br>
* Jupyter Notebook <br>
* Solidity <br>
* Google Colab <br>
* Prophet <br>
* Streamlit <br>
* MetaMask <br>
* Ganache <br>
* Additional library: Random <br>

## Data Analysis:
During our initial data exploratino using Statistica we noticed a sharp decline in ticket revenue and sales starting in 2020 but a significant drop in 2021. This is very clearly associated with COVID-19 protocols and the limitation of audience led games. With restrictions lifting we still want to increase loyalty and ensure people choose to leave the comfort of their home to attend a live game. <br>

![suns image](https://user-images.githubusercontent.com/98990090/185029046-07a49104-0a7f-44b2-b57d-b79c15040cc9.png)<br>
* This graph shows a decline in ticket revenue starting at 2020 and peak decline in the 2021 season largely due to COVID restrictions. The NBA still has strong revenue streams associated with merchandising, advertising, and television contracts which is why total revenue remained steady even though ticket revenue declined so severely.
<br>

![image](https://user-images.githubusercontent.com/98990090/185029279-51736c3f-6275-42b7-a42a-e1bbb112409f.png) <br>
* This graph shows even though Ticket Revenue was at an all time low in ‘21, total revenue was still higher than in ‘11 - ‘16<br>

![image](https://user-images.githubusercontent.com/98990090/185029416-e3c949ed-989d-4ca4-857e-76c23f0e7544.png) <br>
  
# NEED TO ADD INFO ON THIS GRAPH

## Facebook Prophet Analysis:
 <br>
We chose to do Ticket Revenue alone for our predictive analysis as that's the weakest point of the revenue stream right now for the Suns. Even though the tail end of the 2020 season and all of 2021 were a result of COVID - 19 there was already a natural small decline happening in ticket revenue starting after the 2017 season.




# Remix Application:
We used Remix to build our Season Ticket contracts that allows a user to purchase, register, and eventually flip the NFT for sale. The .sol file can be compiled and then deployed error free.

# Streamlit Application:
Our decentralized application allows the user to see the different packages available for purchase and what is included. As stated above in the background tab - we will have Standard, Ultra, and a VIP package available for purchase.

![image](https://user-images.githubusercontent.com/98990090/185030035-6c34f482-bed0-4eea-909e-6b05baa0288c.png)<br>
* **Account users can see the packages, cost, their account balance, and the images available as NFT's.**<br>

![balance of acount and how many nfts](https://user-images.githubusercontent.com/98990090/185031088-f5c7bf57-2127-49f1-8baf-ccf7b94cee13.png)<br>
* **Account balance** <br>

![not enough funds](https://user-images.githubusercontent.com/98990090/185031166-6d8578b1-8102-43c4-891f-2c788fd75621.png)<br>
* **There is a fail safe if someone does NOT have enough in their balance to purchase a package they will receive this error.** <br>

![transaction hash](https://user-images.githubusercontent.com/98990090/185031237-6896e41a-a7ba-43ba-b942-4a35a805adb6.png) <br>
* **Transaction hash receipt of purchasing the NFT** <br>

![image generated](https://user-images.githubusercontent.com/98990090/185031292-44628fb3-a5b2-4c2a-86d0-e5c95cc8330d.png)<br>
* **NFT image generated upon registering the NFT** <br>

![image](https://user-images.githubusercontent.com/98990090/185031417-87f642c6-a966-4895-b513-737f34f49cdc.png) <br>
* **How many NFT's are associated with this specific address - also shows the token ID associated with the NFT and the account owner address**







GOOGLE COLAB LINK: https://colab.research.google.com/drive/1sjd4puCJURcCCgjzKbWQH53CCvBE0Wrg?usp=sharing
