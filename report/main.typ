
// This is a minimal starting document for tracl, a Typst style for ACL.
// See https://typst.app/universe/package/tracl for details.


#import "@preview/tracl:0.7.0": *
#import "@preview/pergamon:0.5.0": *
#import "@preview/dashy-todo:0.1.3": todo



#show: doc => acl(doc,
  anonymous: false,
  title: [A Paper on the Polarisation of the Swahili and the English languages],
  authors: (
    (
      name: "Abdulrasheed Fawole",
      affiliation: [African Institute for Mathematical Sciences (AIMS), South Africa],
      email: "abdulrasheed@aims.ac.za",
    ),
  ),
)


#abstract[
  #lorem(50)
  #todo[Add the abstract at the end of the paper writing]
]


= Introduction

#lorem(80)

= Methodology

#lorem(80)

= Result

#lorem(150)

= Conclusion

#lorem(80)


// Uncomment this to include your bibliography

/*
#add-bib-resource(read("custom.bib"))
#print-acl-bibliography()
*/
