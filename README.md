# IMS-Python
This is a small inventory management system (IMS) built in Python for my course project.

აღწერა ქართულად: 

მოცემული პროგრამა წარმოადგენს მარაგების მართვის მარტივ პროგრამას.
პროგრამას ამჟამად ინტერფეისი არ აქვს და მისი ფუნქციონალი სრულად
იმართება ტერმინალიდან, თუმცა სამომავლოდ (ფინალური პროექტისთვის)
ვგეგმავ ინტერფეისის დამატებას. ინტერფესისი შესაძლო სტრუქტურა უკვე 
აწყობილია კოდში და გვაქვს შემდეგი ფანჯრები:

1. Home - ფანჯარა
    მოცემული ფანჯარა იხსნება პროგრამის გაშვებისას. ამ ფანჯრიდან
    შეგვიძლია დავასრულოთ პროგრამაზე მუშაობა ან გადავიდეთ ძებნის
    ფანჯარაში (Search Window)


პროგრამას ამჟამად აქვს შემდეგი ძირითადი ფუნქციონალი:

1. თუ პროგრამა პირველად გაეშვება ახალ კომპიუტერზე ის ავტომატურად
შექმნის ბაზის (dbs) და ლოგების საქაღალდეებს (logs). იმ შემთხვევაში, 
თუ ეს საქაღალდეები უკვ არსებობს (თუ პროგრამა ერთხელ მაინც 
იყო გაშვებული) მოცემულ კომპიუტერზე მაშინ პროგრამა არაფერს არ 
გააკეთებს.
