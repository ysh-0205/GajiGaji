document.addEventListener('DOMContentLoaded', function () {
  const idTitle = document.getElementById("id_title");
  const idContent = document.getElementById("id_content");
  const idImage = document.getElementById("id_head_image");
  const idAuthor = document.getElementById("id_author");
  const idCategory = document.getElementById("id_category");


  idContent.className = "form-control";
  idImage.className = "form-control";
  idCategory.className = "form-control";




  const contentLabel = idContent.previousElementSibling;
  contentLabel.className = "form-label";

  const idImageLabel = idImage.previousElementSibling;
  idImageLabel.className = "form-label";

  const idAuthorLabel = idAuthor.previousElementSibling;
  idImageLabel.className = "form-label";

  const idCategoryLabel = idCategory.previousElementSibling;
  idImageLabel.className = "form-label";
});


function searchPost(){
    let searchValue = document.getElementById('search-input').value.trim();
    if (searchValue.length > 1){
        location.href="/blog/search/" + searchValue + "/";
    }
    else{
        alert('검색어('+ searchValue +')가 너무 짧습니다.');
    }
};



