const titleElem = document.getElementById("title");
const descriptionElem = document.getElementById("description");
const priorityElem = document.getElementById("priority");
const statusElem = document.getElementById("status");
const startDateElem = document.getElementById("startDate");
const endDateElem = document.getElementById("endDate");
const todoIdElem = document.getElementById("todo_id");
const submitBtnElem = document.getElementById("submit");
const updateBtnElem = document.querySelectorAll(".edit__todo");
const deleteBtnElem = document.querySelectorAll(".delete");
const idPlaceholderElem = document.getElementById("idPlaceholder");

window.onload = () => {
  console.log("document loaded");
  titleElem.value = "";
  descriptionElem.value = "";

  //   startDateElem.value = "";
  //   endDateElem.value = "";
};

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.startsWith(name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

submitBtnElem.addEventListener("click", (event) => {
  event.preventDefault();
  console.log(event.target.textContent);

  if (event.target.textContent.toLowerCase() === "submit") {
    addTodo();
  } else if (event.target.textContent.toLowerCase() == "update") {
    const todo_id = idPlaceholderElem.dataset.idPlaceholder;
    updateTodo(todo_id);
  } else {
    console.log("Bad input");
  }
});

deleteBtnElem.forEach((element) => {
  element.addEventListener("click", (event) => {
    // event.preventDefault();
    // console.log();
    const todo_id = event.target.dataset.todoid;
    deleteTodo(todo_id);
  });
});
updateBtnElem.forEach((element) => {
  element.addEventListener("click", (event) => {
    const todo_id = event.target.dataset.todoid;
    //   event.preventDefault();
    //   const todo_id = todoIdElem.value;
    fetchTodo(todo_id);
  });
});
const addTodo = () => {
  fetch("http://localhost:8000/add/todo", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: JSON.stringify({
      title: titleElem.value,
      description: descriptionElem.value,
      priority: priorityElem.value,
      status: statusElem.value,
      start_date: startDateElem.value,
      end_date: endDateElem.value,
    }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {})
    .catch((error) => {
      console.log(error.message);
    });
};

const fetchTodo = (todo_id) => {
  fetch(`http://localhost:8000/fetch/todo/${todo_id}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
    },
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      const { description, title, status, priority, start_date, end_date } =
        data.payload.fields;
      titleElem.value = title;
      descriptionElem.value = description;
      priority.value = priority;
      statusElem.value = status;
      startDateElem.value = start_date;
      endDateElem.value = end_date;
      idPlaceholderElem.dataset.idPlaceholder = data.payload.pk;
      submitBtnElem.innerHTML = "Update";
      console.log(data.payload);
    })
    .catch((error) => {
      console.log(error.message);
    });
};
const updateTodo = (todo_id) => {
  fetch(`http://localhost:8000/update/todo/${todo_id}/`, {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: JSON.stringify({
      title: titleElem.value,
      description: descriptionElem.value,
      priority: priorityElem.value,
      status: statusElem.value,
      start_date: startDateElem.value,
      end_date: endDateElem.value,
    }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      const { description, title, status, priority, start_date, end_date } =
        data.payload.fields;
      titleElem.value = title;
      descriptionElem.value = description;
      priority.value = priority;
      statusElem.value = status;
      startDateElem.value = start_date;
      endDateElem.value = end_date;
      idPlaceholderElem.dataset.idPlaceholder = data.payload.pk;
      submitBtnElem.innerHTML = "Update";
      console.log(data.payload);
    })
    .catch((error) => {
      console.log(error.message);
    });
};

const deleteTodo = (todo_id) => {
  fetch(`http://localhost:8000/delete/todo/${parseInt(todo_id)}/`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
    },
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log(data);
    })
    .catch((error) => {
      console.log(error.message);
    });
};
