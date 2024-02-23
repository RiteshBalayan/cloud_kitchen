import React, {
  createContext,
  ReactNode,
  useState,
  Dispatch,
  SetStateAction,
} from "react";




interface AppContextValue {

  /**
 * The AppContextValue interface defines the structure for the context value used throughout the application.
 * It is designed to manage the state and actions related to UI components like headers, sign-in forms, category filters,
 * sidebars, and more. This interface ensures that the context provides both the current state (boolean flags) and
 * functions to update those states (setters), allowing for a consistent and type-safe way to manage and distribute
 * application-level state.
 * 
 * Properties:
 * - headerClass: A boolean flag indicating the state of a header class (e.g., whether a specific class is applied).
 * - showSignInForm: A boolean flag indicating whether the sign-in form should be displayed.
 * - showCategeryFilter: A boolean flag indicating whether the category filter UI should be shown.
 * - showSidebar: A boolean flag indicating whether the sidebar is visible.
 * - headerSidebar: A boolean flag indicating a specific state or mode for the sidebar related to the header.
 * 
 * Methods (setters):
 * - setHeaderClass: Function to update the headerClass state.
 * - ...
 */

  headerClass: boolean;
  setHeaderClass: Dispatch<SetStateAction<boolean>>;
  showSignInForm: boolean;
  setShowSignInForm: Dispatch<SetStateAction<boolean>>;
  showCategeryFilter: boolean;
  setShowCategeryFilter: Dispatch<SetStateAction<boolean>>;
  showSidebar: boolean;
  setShowSidebar: Dispatch<SetStateAction<boolean>>;
  headerSidebar: boolean;
  setHeaderSidebar: Dispatch<SetStateAction<boolean>>;
}

const defaultState: AppContextValue = {
  headerClass: false,
  setHeaderClass: () => {},
  showSignInForm: false,
  setShowSignInForm: () => {},
  showCategeryFilter: false,
  setShowCategeryFilter: () => {},
  showSidebar: false,
  setShowSidebar: () => {},
  headerSidebar: false,
  setHeaderSidebar: () => {},
};

export const Context = createContext(defaultState);

interface AppContextProviderProps {
  children: ReactNode;
}

export const AppContextProvider: React.FC<AppContextProviderProps> = ({
  children,
}) => {
  const [headerClass, setHeaderClass] = useState(false);
  const [showSignInForm, setShowSignInForm] = useState(false);
  const [showCategeryFilter, setShowCategeryFilter] = useState(false);
  const [showSidebar, setShowSidebar] = useState(false);
  const [headerSidebar, setHeaderSidebar] = useState(false);

  const contextValue: AppContextValue = {
    headerClass,
    setHeaderClass,
    showSignInForm,
    setShowSignInForm,
    showCategeryFilter,
    setShowCategeryFilter,
    showSidebar,
    setShowSidebar,
    headerSidebar,
    setHeaderSidebar,
  };

  return <Context.Provider value={contextValue}>{children}</Context.Provider>;
};
