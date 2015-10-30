[![][1]][2]

Ever since it first aired in July 1989, Seinfeld has been amongst the best TV shows of all time. Who'd have thought that someday, an amazing product might just have something to do with the show, even if it's just an indirect reference?

Except that it did happen. Enter [Postman][3].

Today's landscape is all about building APIs for your product ­ either as a core component, or as an add­on to help users integrate your product with other services. But like most ubiquitous ideologies out there, the traditional framework for building APIs is broken, with the most significant issue being that at the end of the day, API developers have no way to communicate changes amongst themselves, and it's not exactly easy for API consumers to just pick up your API and roll with it.

This is where Postman's changing the way API development goes forward, across small teams and enterprises. The whole concept of Postman is to make the idea of building an API and working with it, an extremely efficient process. It dramatically cuts down the time and effort required to communicate API changes and testing them out ­ all this contributes towards a cleaner development cycle. Happier devs. And of course, happier API consumers.

![Ankit Sobti][4] *Ankit Sobti*

A conversation with Ankit Sobti, the co­founder and CTO of Postman revealed a treasure trove about how Postman came into existence, and how it's managed to scale to about 2M users across the globe, with users as diverse as small startup teams, to large enterprises building APIs for public consumption ­ and all of it, with a smaller team than we'd realize.

* * *

![Abhinav Asthana][5] *Abhinav Asthana*

Ankit himself has had an interesting ride. After graduating from Netaji Subhash Institute of Technology back in 2009, he worked with Adobe and Yahoo, where he met Abhinav Asthana, who'd go on to build the first version of Postman. It was at Yahoo, where they first ran into the issues surrounding API development.

"At Yahoo, while building their content management system, we'd end up building frontends for our APIs, and run into scenarios where someone would make a change to one particular portion of the API, and nobody would know ­ until the API broke," recounts Ankit. "At the end of the day, documentation was also a pain ­ and it's hard to document APIs when you're trying to move fast."

After his stints at Yahoo and Adobe, Ankit went for an MBA from the Indian School of Business ("I happen to be the only MBA in the company," he laughs), while Abhinav went on to work with TeliportMe, a panoramic photo app. After facing the same issues, he decided to build something that would help him improve his API workflow ­ and Postman was born, as a simple Chrome extension, a sort of UI for cURL, the age­old Unix HTTP client.

In the meantime, after wrapping up his MBA, Ankit had offers from the likes of Microsoft and Amazon, but he went for a slightly lesser­ known company in Mumbai - Directi.

"The CTO sat down and explained the problem to me. I'm like, fuck let's do it, it's fun. The idea was challenging - Directi's division Media.net was looking at building a contextual real­time platform for ad bids. It's a fairly complex problem - you hit a web page, an ad is loaded - this is where an auction takes place, to decide what ad's displayed. You need to calculate an expected revenue from showing a particular ad to a particular person. As long as it's greater than the cost you quote for the bid, there's a business. The problem is that mathematically, it's an inequality with no constants - it's impossible to solve deterministically. By the time I left, this was running as a profitable business."

In the meantime, Ankit kept working on Postman - contributing code, building an analytics tool called Sherlock to track who was talking about Postman, and helping out with product strategy.

Finally, in September 2014, Abhinav and Ankit took up Postman full­time. It made perfect sense; there was a definite problem that Postman was solving, which was the informational asymmetry between API producers, and API consumers. This led to the next version of Postman being released. This also saw Abhijeet Kane joining up, and ultimately becoming a co­founder himself.

![Abhijeet Kane][6] *Abhijeet Kane*

"Abhijeet was so good, we could not *not* deem him a co­founder. He's an asset - as a co­founder and as a developer. And with him onboard, that's when Postman really started."

* * *

## The isomorphic tech stack

So why take the Chrome app path?

"Cross­-platform, plus Javascript. Postman as a Chrome app allows you to make cross-­origin requests. The other alternative is using a server­-side proxy - but that would involve all data to be routed through our servers, which requires an inherent trust. With the number of requests that go through, a client­-side app makes more sense, or we'd never have been able to scale. Chrome's actually a very, very decent platform. There are quirks that are annoying, but on the whole, it's a great platform to build cross­-platform apps. And back then, there weren't any great tools to build such apps. Now there's Electron, which powers the Atom editor, and allows you to build high­-performant native apps. We've just launched a beta version of Postman on OSX using Electron."

Right now, Ankit et al are busy working on Postman Sync - a platform that allows you to backup and share your Postman Collections, the core data generated by Postman, onto the cloud. These are essentially units that help you group individual HTTP requests together, as well as their sample responses. It's like Google Drive, where collections can be shared with other devs, and everyone can see where the API was at one particular point in time, and where it's headed. The best part is that Postman is recursively built using ­- yes, you guessed right, Postman. ￼￼ But that's just one aspect where Postman changes things. Documentation is the one pain point that's still not easy to deal with. This is where collections step up and prove their mettle. They intrinsically serve as executable units of documentation, where you can attach hooks at the beginning of the request, and at the end of the API response. This makes Postman collections self­-aware, self­-executing units, which anyone can pick up, to learn about an API, even play with it.

A lot of client-­side Javascript is utilized at Postman, but there are also servers written in Node.js, for Postman's Sync platform, that allow you to see updates on an API's development, and foster collaboration between API producers working on the same code.

One of the interesting aspects of Postman's tech stack is isomorphism: as Ankit puts it, about 85% of the code on the Postman server and the client, to facilitate communication, is the same. That is not only an engineering marvel, but also beneficial from a talent perspective ­- isomorphic Javascript means backend devs and front-end experts can write code that works with both. Even more interesting is the relationship between Postman and the popular Node MVC project SailsJS - the Sails devs regularly use Postman, and Postman devs contribute to Sails. "It's a very symbiotic relationship,", says Ankit. "We've got this friendly rapport with them, where we contribute to each other's code bases, and it's quite awesome that way."

On the frontend, Postman has used Backbone, but they're now making the switch to React, Facebook's open-­source reusable components framework. "The idea that you can take a React component, and use it in an expanded form across multiple UIs and platforms is amazing," affirms Ankit. And with React Native's entry, going mobile is now seamless.

Back in its early days, Ankit wrote an analytics tool called Sherlock, which helped track and measure how early users were talking about Postman - which invariably led Ankit and Abhinav to realize that Postman was popping up at universities, tech companies as well as conferences, where people would talk about how they were using Postman in their daily workflow. Back then, Sherlock was built on top of Google Sheets. "What a lot of people don't realize, is that you can script Google Docs and Sheets with Javascript, the way you could script Office documents with VBScript," Ankit mentions. "That allowed us to quickly build a tool that measured Postman's impact, and it let us reach out to our first set of adopters, and turn them into evangelists."

While there's a lot more to Postman's tech, it's worth mentioning here that it all runs on Amazon Web Services, and as Ankit mentions, Amazon's Elastic Load Balancers are amongst the best ever. "Another thing about Amazon is that they make sure you're using their cloud in the right way; we had people from Amazon who came down to our office to make sure we were utilizing Amazon right, which was invaluable."

## Transparency and honesty in design

> "At Postman, we have these core values that we feel are important, for us as a company. That's transparency and honesty, and it's something we try and inculcate in everything we do," says Ankit. "That's the kind of approach we take towards design. We have a dedicated design team, who aren't exactly from an API background, and then there's Abhinav and me, who've got a fair idea about design. We try to implement user flows that mirror our core values, and at the same time, we rely on gut instinct to come to a design decision. So I may not have a particular reason for a particular aspect in Postman's design, but I know it'll work, and it usually does. A lot of input for making Postman's UX better also comes from user feedback, so a combination of all of these factors makes for a user flow that works."

## "Growth is all about instincts, analytics and a great product."

> "When you're reactive, users trust you; they know that if something does go wrong, Postman will respond. And this wins you advocates. They become your advocates at companies, universities, conferences. When you reach out to them, they'll respond, and they'll gladly speak for you."

For Ankit, growth is all about gut instinct-­driven marketing, analytics and a great product. According to him, the best way to tackle growth is to make sure you're building a great product that solves a genuine problem, addresses a genuine need. That, in itself, is a winning growth tactic - it spreads its own word.

What also worked with Postman, was to have a product that's given out for free, and since it solves a pain point, that helps in spreading the word too. Another important factor is reactiveness, in terms of support. "We've responded to support queries at 4AM, in less than an hour," recalls Ankit. "Abhijeet himself handles a lot of support requests, while I look after support for Sync, since I've been building it for the most part. When you're reactive, users trust you; they know that if something does go wrong, Postman will respond. And this wins you advocates. They become your advocates at companies, universities, conferences. When you reach out to them, they'll respond, and they'll gladly speak for you."

Another point worth noting here is that the most (seemingly) annoying customers in your support queue, according to Ankit, are also the ones who depend on your product the most. "That's why they're frequently reaching out to you, and ultimately, with a great product and reactive support, they become your best advocates." This translates into their sales strategy too. "If the end users already love you, convincing the upper echelons of the organizations becomes infinitely easier."

Another advantage that Postman possesses, is that it's inherently viral. "Consider collections, " Ankit points out. "They're a simple JSON file, which you can share with colleagues, so that they can collaboratively work on your API. Now, to run the collection, you need the Postman app, and because it's useful, people install it, and use it. That's like inherent growth, right there." ￼￼ The idea behind growth, for Ankit, is that it's all about making sensible decisions at the right time, and that if you build your product right, solving a genuine universal problem, growth automatically falls into place. "Consider the idea about collections fueling growth," he mentions. "When we worked on them, we weren't thinking about growth at all - but it all just fell into place. It’s about following best practices at all times."

## #brainwaves for product management

How exactly does the team decide on what to add to Postman? "A lot of information for adding features or revamping existing features, comes from inbound channels - especially support. And we've got a Slack channel for ourselves, called #brainwaves - the idea is to come up with possible items and maintain a list of them, and of course, debate about them," says Ankit. "We make sure that we have a detailed and well­-defined roadmap for the next 12 months, so we know exactly what we're doing for the next one year, which something a lot of companies aren't able to do."

Ankit has found it an interesting challenge, to juggle product and tech together. One of the recent hires the company's made is Alex J.V., a young growth pro, who's worked on some interesting projects earlier, including starting up the Firefly unicycle project (Disclaimer - the author has tried out the Firefly and loved it - before falling off it).

"When Alex first joined, he was working on growth, and building up our community, but it quickly became apparent that Alex as a product guy was a great deal, especially because I believe product involves growth. Now we're at a point where Alex handles the product completely, and only today, I got an earful from him about how my tasks are pending - so that worked out fine! He has also built out a fairly comprehensive analytics system with its origins in Sherlock, that allows us make informed decisions around growth, product and design.”

At Postman, features are typically grouped into three broad categories: features that customers face directly, features that are apparent to customers but don't affect them directly, and other items that affect the product as a whole, and are not visible or apparent to end users.

> "From the outset, we engage a lot with our users, and we've got this drip email that's sent out to them, collecting feedback. That works out really well, to make sure customers are able to use Postman without any issues, as well as help them propose new additions. Of course we also get pissed users - and it's a good thing, users being pissed, especially when we mess up - it always brings up valuable insights."

![Postman in action][7] *Working on the notCRUD Community API with Postman*

## "Great products are built by small teams."

> "...we hire for a particular skill that we know we need."

While the team is based out of Bangalore, they're all set to open up an office in San Francisco pretty soon. So how do they envisage tackling a scenario where they've got two offices in different time zones and cultures, working in tandem as a small team for a product that's used on such a massive scale?

"When products scale, typical companies hire managers, and thus end up having multiple levels. But today, great products are usually built by small teams, and hiring a lot of people, especially for managerial roles, isn't something we intend to do. Look at WhatsApp - they scaled to 900M users with a team of just 45." explains Ankit. "As far as the concept of having remote teams work in tandem - it's all about imbibing the culture of working on your own, but in a distributed environment, right from the start. My idea of the ideal product strategy is to have less conversations with everyone involved in building it out, and to have more platforms where the team can just look into and see what needs to be worked upon - for instance, one just has to look at a JIRA board to know that okay, I have to build this, I have to work on that."

How has the recent investment by Nexus changed this? Not much, according to Ankit. "With money, there's always this expectation to hire more, but that's not going to change for us. We've got a great set of investors who agree with us on this point, and at the end, we usually don't hire for a project or a feature we're planning to build - we hire for a particular skill that we know we need."

* * *

It's going to be a very interesting ride, for Postman. Solving a perennial need in the right way is something they've figured out to a large extent. But what's next? Following their journey is going to be very, very scintillating, indeed. In the meantime, the author knows he's going to be using Postman very soon.

 [1]: https://www.getpostman.com/img/whole-logo.png
 [2]: http://www.getpostman.com/
 [3]: https://www.getpostman.com
 [4]: http://originals.notcrud.com/wp-content/uploads/2015/10/1444112343321-ankit.png
 [5]: http://originals.notcrud.com/wp-content/uploads/2015/10/1444112310213-abhinav.png
 [6]: http://originals.notcrud.com/wp-content/uploads/2015/10/1444112273440-abhijeet.png
 [7]: http://originals.notcrud.com/wp-content/uploads/2015/10/Screen-Shot-2015-10-21-at-2.34.05-PM.png