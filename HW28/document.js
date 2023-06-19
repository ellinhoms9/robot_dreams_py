const myDiv = document.createElement("div");
myDiv.id = "buttons";
myDiv.style.textAlign = "right";

btnNames = ["Add to friends", "Write a message", "Offer a job", "Submit homework"];
let buttons = [];
btnNames.map((buttonName, index) => {
    let button = document.createElement("button");
    button.className = "btn btn-success";
    button.innerText = buttonName;
    button.style.margin = "5px";
    button.addEventListener("click", () => {
        if (index === 0) {
            if (!button.disabled) {
                button.disabled = true;
                button.innerText = "Confirmation is pending";
                incrementFriendsCount();
            }
        }
        if (index === 1){
            button.classList.toggle("clicked");

        }
        if (index === 2) {
            if (buttons[0].style.display === "none") {
                buttons[0].style.display = "inline-block";
            } else {
                buttons[0].style.display = "none";
            }
        }
        if (index === 3){
            addNewRow();
        }


    });
    buttons.push(button);
    myDiv.appendChild(button);
});

const friendsCountElement = document.createElement("span");
friendsCountElement.id = "friends-count";
friendsCountElement.innerText = Math.floor(Math.random() * 100);
friendsCountElement.style.position = "absolute";
friendsCountElement.style.top = "5px";
friendsCountElement.style.right = "5px";
myDiv.appendChild(friendsCountElement);

const friendsLabelElement = document.createElement("span");
friendsLabelElement.innerText = "Number of friends: ";
friendsLabelElement.style.position = "absolute";
friendsLabelElement.style.top = "5px";
friendsLabelElement.style.right = "70px";
myDiv.appendChild(friendsLabelElement);

document.getElementsByTagName("div")[0].appendChild(myDiv);

function incrementFriendsCount() {
    const friendsCount = parseInt(friendsCountElement.innerText);
    friendsCountElement.innerText = friendsCount + 1;
}

function addNewRow() {
    const tableBody = document.querySelector("table.my-table tbody");
    const newRow = document.createElement("tr");
    newRow.innerHTML = `
        <th scope="row">24</th>
        <td>New Homework</td>
        <td>0</td>
    `;
    tableBody.appendChild(newRow);
}
