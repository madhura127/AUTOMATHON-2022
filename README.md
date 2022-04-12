# AUTOMATHON-2022

Problem Statement :
Object detection with reduced labeling efforts using Computer vision and Machine Learning.

Background :
Object detection is a computer technology related to computer vision and image processing that deals with identifying and locating instances of objects within images or videos. Image recognition assigns a label to an image. A picture of a dog receives the label “dog”. A picture of two dogs, still receives the label “dog”. Object detection, on the other hand, draws a box around each dog and labels the box “dog”. 
 In more traditional ML-based approaches, computer vision techniques are used to look at various features of an image that may belong to an object. These features are then fed into a regression model that predicts the location of the object along with its label. Data labeling refers to the process of adding tags or labels to raw data such as images, videos, text, and audio. Successful machine learning models are built on the shoulders of large volumes of high-quality training data. Hence, labeling data is the first and most significant part of object detection, the more dedication you will give in labeling images, the more accurate your model can be. But this process of labeling is often complicated and very time-consuming.Here, we will be discussing the complete approach of labeling and how can we make it more efficient in detail.

Approach :
Data labeling approaches :
There are various labeling approaches. depending on the problem statement, the time frame of the project, and the number of people who are associated with the work.The most common approaches are:
In-house :  This is when your data labelers are your in-house team of data scientists. This approach has a number of immediate benefits: tracking progress is simple, and accuracy and quality levels are reliable but the time taken to annotate increases drastically, resulting in the entire data labeling process and cleaning being very slow.
Crowdsourcing  :  Crowdsourcing  platforms are a way to enlist help from people across the globe to work on particular tasks. Because crowdsourcing  jobs can be picked up from anywhere in the world and performed as tasks become available, it is extremely quick and cost effective. However, crowdsourcing platforms can vary wildly in terms of worker quality and worker management.
Outsourcing : Outsourcing is a middle ground between crowdsourcing and in-house data labeling where the task of data annotation is outsourced to an organization or an individual. This approach of building up annotation datasets is perfect for projects that do not have much funding, yet require a significant quality of data annotation.

Common types of data labeling
Data annotations in computer vision can be of various types, depending on the visual task that we want the model to perform. 

Image Classification: Data annotation for image classification entails the addition of a tag to the image being worked on. The number of unique tags in the entire database is the number of classes that the model can classify. It solves the problem of intra-class variation.

Image Segmentation: In Image Segmentation, the task of the Computer Vision algorithm is to separate objects in the images from their backgrounds and other objects in the same image.For instance, green screen can be used to detect contours of object.

Object Detection: Object Detection refers to the detection of objects and their locations via computer vision.

Pose estimation: Pose estimation refers to the use of Computer Vision tools to estimate the pose of a person in an image.Pose estimation runs by the detection of key points in the body and correlating these key points for obtaining the pose.

Conclusion :
Successful machine learning models are built on the shoulders of large volumes of high-quality training data. But, the process to create the training data necessary to build these models is often expensive, complicated, and time-consuming.The majority of models created today require a human to manually label data in a way that allows the model to learn how to make correct decisions. To overcome this challenge, labeling can be made more efficient by using a machine learning model to label data automatically. 

