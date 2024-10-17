function toggleMenu(){
    const menu = document.querySelector('.sub_wrap')
    menu.classList.toggle('hide');

    document.addEventListener('click', () => {
        const menuBtn = document.querySelector('.menuBar');
        const menu = document.querySelector('.sub_wrap');

        if (!menu.contains(e.target) && !menuBtn.contains(e.target)) {
            menu.classList.add('hide');
            }
        });

    document.activeElement('click', e => {
        if(!menu.contains(e.target) && e.target !== menuBtn) {
            menu.classList.add('hide');
        }
    })
}

const selectedLinks = document.querySelectorAll('.link-item');

selectedLinks.forEach(navLinkEl => {
    navLinkEl.addEventListener('click', () => {
            document.querySelector('.active')?.classList.remove('active');
            navLinkEl.classList.add('active');
        });
});

// function changeContent(){
//     var content = document.querySelectorAll('list')
//     content.classList.toggle('hide');

//     document.addEventListener('click'), 
// }

// for (var i = 0; i < li_elements.length; i++) {
//     li_elements[i].addEventListener("click", function() {
//       li_elements.forEach(function(li) {
//         li.classList.remove("active");
//       });
//       this.classList.add("active");
//       var li_value = this.getAttribute("data-li");
//       item_elements.forEach(function(item) {
//         item.style.display = "none";
//       });
//       if (li_value == "angular") {
//         document.querySelector("." + li_value).style.display = "block";
//       } else if (li_value == "nodejs") {
//         document.querySelector("." + li_value).style.display = "block";
//       } else if (li_value == "reactjs") {
//         document.querySelector("." + li_value).style.display = "block";
//       } else if (li_value == "vuejs") {
//         document.querySelector("." + li_value).style.display = "block";
//       } else {
//         console.log("");
//       }
//     });
//   }