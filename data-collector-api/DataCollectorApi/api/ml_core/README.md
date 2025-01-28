# `ml_core` Package

The `ml_core` package is designed to provide modular and reusable components for data preprocessing, model management, sentiment analysis, topic modeling, community detection, and utility functions. Each submodule contains classes following best practices and incorporating design patterns to ensure **extensibility**, **scalability**, and **ease of maintenance**.

---

## Package Structure

### 1. `data_preprocessing`
   - `data_cleaner.py`
     - `DataCleaner` - Implements the **Strategy Pattern** to allow interchangeable data-cleaning strategies (e.g., stopword removal, slang handling).
   - `data_loader.py`
     - `DataLoader` - Uses the **Factory Method Pattern** to load data from various sources, such as CSV files, databases, or APIs.
   - `data_transformer.py`
     - `DataTransformer` - Follows the **Template Method Pattern** to ensure consistent data transformation steps, with customizable processes like normalization and tokenization.
   - `data_splitter.py`
     - `DataSplitter` - Applies the **Singleton Pattern** to manage data splits consistently across the application.

---

### 2. `evaluation`
   - `evaluator.py`
     - `Evaluator` - Implements the **Strategy Pattern** to enable various evaluation strategies, like `PrecisionEvaluator`, `RecallEvaluator`, etc.
   - `confusion_matrix.py`
     - `ConfusionMatrix` - Uses the **Factory Method Pattern** to generate confusion matrices based on model type and results format.
   - `metrics_calculator.py`
     - `MetricsCalculator` - Follows the **Adapter Pattern** to interface with different metric libraries for evaluation consistency.

---

### 3. `models`
   - `model_factory.py`
     - `ModelFactory` - Uses the **Abstract Factory Pattern** to produce different types of models, including sentiment analysis, topic modeling, and community detection.
   - `sentiment_model.py`
     - `SentimentModel` - Applies the **Decorator Pattern** for added functionalities like caching or performance tracking on top of the base sentiment model.
   - `topic_model.py`
     - `TopicModel` - Uses the **Prototype Pattern** to allow for modified instances without affecting the base model configuration.
   - `community_detection_model.py`
     - `CommunityDetectionModel` - Follows the **Composite Pattern** to model complex network structures and community hierarchies.

---

### 4. `sentiment_analysis`
   - `sentiment_analyzer.py`
     - `SentimentAnalyzer` - Implements the **Facade Pattern** to provide a simplified interface for different sentiment analysis methods.
   - `lexicon_based_analyzer.py`
     - `LexiconBasedAnalyzer` - Is responsible for analyzing the sentiment of text using lexicon-based methods.
   - `deep_learning_analyzer.py`
     - `DeepLearningAnalyzer` - Handles sentiment analysis using deep learning models.

---

### 5. `topic_modeling`
   - `topic_modeler.py`
     - `TopicModeler` - Uses the **Facade Pattern** to provide a unified interface for various topic modeling techniques (e.g., LDA, LSA).
   - `lda_model.py`
     - `LDAModel` - Applies the **Builder Pattern** to construct specific LDA model configurations.
   - `lsa_model.py`
     - `LSAModel` - Also uses the **Builder Pattern** to construct LSA model configurations.
   - `topic_visualizer.py`
     - `TopicVisualizer` - Implements the **Observer Pattern** to update visualizations as topics change.

### 6. `community_detection`
   - `community_detector.py`
     - `CommunityDetector` - Implements the **Facade Pattern** to simplify access to different community detection algorithms.
   - `modularity_calculator.py`
     - `ModularityCalculator` - Uses the **Template Method Pattern** to calculate modularity for different algorithms.
   - `graph_builder.py`
     - `GraphBuilder` - Follows the **Builder Pattern** to help construct complex graph structures for network analysis.
   - `community_visualizer.py`
     - `CommunityVisualizer` - Applies the **Observer Pattern** to notify views when community structures are updated.

### 7. `utils`
   - `logger.py`
     - `Logger` - Uses the **Singleton Pattern** to ensure a single logging instance across the application.
   - `config_loader.py`
     - `ConfigLoader` - Follows the **Singleton Pattern** to maintain consistent configuration loading.
   - `performance_tracker.py`
     - `PerformanceTracker` - Implements the **Observer Pattern** to track and update performance metrics for registered observers.

---

## Design Pattern Summary

- **Singleton**: Ensures only one instance of utilities such as Logger and ConfigLoader.
- **Strategy**: Provides flexible strategies for interchangeable processes (e.g., data cleaning, evaluation).
- **Factory Method & Abstract Factory**: Enables modular data loading and model creation.
- **Facade**: Simplifies complex subsystems (e.g., sentiment analysis, topic modeling).
- **Adapter**: Allows for different metric formats compatibility in the evaluation module.
- **Template Method**: Standardizes steps in processing methods (e.g., data transformation, modularity calculations).
- **Builder**: Facilitates the flexible creation of structured models and configurations.
- **Observer**: Notifies components about data or performance updates, ensuring a responsive architecture.
- **Decorator**: Adds functionalities dynamically to base classes without altering their structure.
- **Composite**: Represents hierarchical structures of models or communities uniformly.
- **Prototype**: Allows for creating modified instances without affecting the base model configuration.