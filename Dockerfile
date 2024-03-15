FROM maven:3.8.5-openjdk-17 AS build
COPY ITCluster2024/ITCluster2024 .
RUN mvn clean package -DskipTests

FROM openjdk:17.0.1-jdk-slim
COPY --from=build /target/ITCluster2024-0.0.1-SNAPSHOT.jar ITCluster2024.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "ITCluster2024.jar"]