// import React from "react";

// const StructuredData = () => {
//     const jsonLd = {
//         "@context": "https://schema.org",
//         "@type": "WebSite",
//         "name": "Migration reporting tool",
//         "url": "http://35.228.54.3:5173/",
//         "description": "Our website presents information about the migration of birds, humans and aliens.",
//         "author": {
//             "@type": "Person",
//             "name": "Grey Heron"
//         }
//     };

//     return (
//         <script type="application/ld+json">
//             {JSON.stringify(jsonLd)}
//         </script>
//     );
// };

// export default StructuredData;



import { useEffect } from "react";

const StructuredData = () => {
    useEffect(() => {
        const script = document.createElement("script");
        script.type = "application/ld+json";
        script.textContent = JSON.stringify({
            "@context": "https://schema.org",
            "@type": "WebSite",
            "name": "Migration reporting tool",
            "url": "http://35.228.54.3:5173/",
            "description": "Our website presents information about the migration of birds, humans and aliens.",
            "author": {
                "@type": "Organization",
                "name": "Grey Heron"
            }
        });

        document.head.appendChild(script);

        return () => {
            document.head.removeChild(script);
        };
    }, []);

    return null;
};

export default StructuredData;
